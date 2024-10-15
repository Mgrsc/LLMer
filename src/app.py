import chainlit as cl
from config import (get_content_for_starter,
                    get_model_for_profile,
                    prompt_dict,
                    CHAT_SETTINGS,
                    LLM)
from utils.logger import logger
from chainlit.config import config

# setting default tag and history
@cl.on_chat_start
def start_chat():
    cl.user_session.set("is_new_session", True)

# Construct a new conversation setting system prompt.
async def handle_new_session(user_input: str):
    matched = False
    for starter in await config.code.set_starters():
        if user_input == starter.message:
            matched = True
            content = get_content_for_starter(starter.label)
            cl.user_session.set("message_history", [{"role": "system", "content": content}])
            break

    if not matched:
        default_prompt = next(iter(prompt_dict.values()), "Can I help you?")
        cl.user_session.set("message_history", [{"role": "system", "content": default_prompt}])

    cl.user_session.set("is_new_session", False)

# main logic ,receive message will call this function
@cl.on_message
async def main(message: cl.Message):
    is_new_session = cl.user_session.get("is_new_session", False)

    # Get and update message history
    message_history = cl.user_session.get("message_history")


    # If it is a new session, get prompt
    if message_history is None or is_new_session:
        await handle_new_session(message.content)
        message_history = cl.user_session.get("message_history")
        logger.info("Start a new session or initialize if not yet.")


    # Append user_message to history
    message_history.append({"role": "user", "content": message.content})
    logger.info(f"Message History: {message_history}")

    msg = cl.Message(content="")
    await msg.send()

    # set used model
    chat_profile = cl.user_session.get("chat_profile")
    model = get_model_for_profile(chat_profile)
    logger.info(f"Using model: {model}")

    # create stream send message
    try:
        stream = await LLM.chat.completions.create(
            messages=message_history, stream=True, model=model, **CHAT_SETTINGS
        )

        full_response = ""
        async for part in stream:
            if not part.choices:
                continue

            delta = part.choices[0].delta
            if not delta:
                continue

            content = getattr(delta, 'content', None)
            if content:
                full_response += content
                await msg.stream_token(content)
            elif hasattr(delta, 'finish_reason'):
                break


        message_history.append({"role": "assistant", "content": full_response})
        await msg.update()
    except Exception as e:
        logger.error(f"Error during LLM completion: {e}")
        await msg.update(content="Sorry, an error occurred while processing your request. Please try again later.")

