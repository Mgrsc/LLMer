import os
import toml
from openai import AsyncOpenAI
import chainlit as cl

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
config_path = os.path.join(root_dir, 'config.toml')
with open(config_path, 'r', encoding='utf-8') as config_file:
    config = toml.load(config_file)


logging_enabled = config.get('LOGGING_ENABLED', False)
log_dir = config.get('LOG_DIR', 'logs')

LLM = AsyncOpenAI(
    api_key=config.get('OPENAI_API_KEY'),
    base_url=config.get('OPENAI_BASE_URL')
)


CHAT_SETTINGS = config.get('CHAT_SETTINGS', {
    "temperature": 0,
    "max_tokens": 4096,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
})

prompts = config.get('PROMPTS', {})

prompt_dict = prompts

starters = config.get('STARTERS', {})

# set starters
@cl.set_starters
async def choice_role():
    starter_list = []
    i = 1
    icon_path = "/public/icons/"
    while f'START_{i}_LABEL' in starters:
        starter_list.append(
            cl.Starter(
                label=starters.get(f'START_{i}_LABEL', f"label{i}"),
                message=starters.get(f'START_{i}_MESSAGE', f"message{i}"),
                icon=icon_path + starters.get(f'START_{i}_ICON', 'zhexue.webp')
            )
        )
        i += 1
        print(starter_list)
    return starter_list

# Get the prompt of the corresponding role
def get_content_for_starter(label: str) -> str:
    content_mapping = {}
    i = 1
    while f'START_{i}_LABEL' in starters:
        prompt_key = f'PROMPT_{i+1}'
        content_mapping[starters.get(f'START_{i}_LABEL', "Hello")] = prompts.get(prompt_key, f"you are assistant")
        i += 1

    default_prompt = next(iter(prompt_dict.values()), "Can I help you?")
    return content_mapping.get(label, default_prompt)

# setting profiles
@cl.set_chat_profiles
async def chat_profile():
    profiles = []
    icon_path = "/public/model/"
    for model_key, model_info in config.get('MODEL_MAP', {}).items():
        profiles.append(cl.ChatProfile(
            name=model_info.get('profile_name', 'Deepseek'),
            markdown_description=model_info.get('markdown_description', 'error'),
            icon=icon_path + model_info.get('icon', 'openai.svg')
        ))
    return profiles

# get model for profile
def get_model_for_profile(chat_profile: str) -> str:
    for model_info in config.get('MODEL_MAP', {}).values():
        if model_info.get('profile_name') == chat_profile:
            return model_info.get('model_name', 'gpt-4o-mini')
    return "gpt-4o-mini"


