# LLMER

This project allows you to customize the Prompt for each starter, optimizes the UI using CSS, and provides a Docker image for easy deployment. Simply configure the config.json for out-of-the-box use. Below are the instructions on how to set up and run this project.

## Table of Contents 📚

- [Installation and Configuration](#installation-and-configuration)
- [Docker Deployment](#docker-deployment)
- [Contributions](#contributions)
- [License](#license)

## Installation and Configuration 🚀

1. **Install `uv`**
    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2. **Configure config.toml**
```
[MODEL_MAP]
[[MODEL_MAP]."{name}"] # Corresponds to a model
profile_name = "Model A" # Displayed model name
model_name = "model-a" # Actual model name
markdown_description = "Description of Model A" # Model description
icon = "/public/model/model-a.svg" # Model icon

# Starter settings, up to four starters
[STARTERS] 
START_1_LABEL = "Professional Copywriting Assistant" # Content displayed for starter in UI
START_1_MESSAGE = "Help me write a copy! Master" # Message sent when starter is launched
START_1_ICON = "/public/icons/copywriter.webp" # Starter icon

# One prompt corresponds to one starter, the first prompt_1 is the default prompt
# Starting from the second, prompt_2 corresponds to the first prompt of the starter, must match the number of starters
# Default prompt: (prompt_1); starter: (prompt_2, prompt_3, prompt_4, prompt_5) up to four
[PROMPTS]
PROMPT_1 = """
xxxxxx
"""

```

3. **Sync Environment**
    ```sh
    uv sync
    ```

4. **Run the Project**
    ```sh
    cd src
    uv run -- chainlit run app.py -w --host 0.0.0.0 --port 8000
    ```
    - The `--host` and `--port` parameters are optional and can be adjusted as needed. Refer to [chainlit](https://docs.chainlit.io/backend/command-line) for details.

## Docker Deployment 🐳

### Docker
```shell
mv config.toml.exp config.toml
# Modify .env as needed
docker run -d -p 8000:8000 -v ./config.toml:/app/config.toml bitfennec/llmer:latest
```
Visit `http://localhost:8000` to view the running application.

### Docker Compose

```shell
git clone https://github.com/Mgrsc/llmer.git
cd llmer
```
Edit docker-compose.yaml as needed
```yaml
services:
  llmer:
    image: bitfennec/llmer:latest
    container_name: llmer
    ports:
      - 30004:8000
    volumes:
      - ./config.toml:/app/config.toml
      # - ./src/public/model:/app/src/public/model # Optional, if you need to add icons
```
```shell
docker-compose up -d
```

Visit `http://localhost:8000` to view the running application.

## Contributions 🤝

If you have any suggestions for improvements or want to report issues, feel free to submit an issue or pull request (PR).

## License 📄

This project is based on [Chainlit](https://github.com/Chainlit/Chainlit) and uses the Apache 2.0 license. For more details, please refer to the [LICENSE](./LICENSE) file.