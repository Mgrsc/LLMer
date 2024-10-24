# LLMER
该项目让你能够自定义每个启动器（starter）的Prompt，使用css优化了ui，并提供Docker image，方便部署，仅需配置config.json，开箱即用。下面是如何设置和运行这个项目的说明。

## 目录 📚

- [安装和配置](#安装和配置)
- [Docker 部署](#docker-部署)
- [贡献](#贡献)
- [许可证](#许可证)


## 安装和配置 🚀
1. **安装 `uv`**
    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2. **配置config.toml**
```
[MODEL_MAP]
[[MODEL_MAP]."{name}"] #对应一个模型
profile_name = "Model A" # 显示的模型名字
model_name = "model-a" # 真实的模型名字
markdown_description = "Description of Model A" # 模型描述
icon = "model-a.svg" # 模型图标，默认存放在model下

# starter设置，最多四个starter
[STARTERS]
START_1_LABEL = "专业文案助手" # starter在ui显示的内容
START_1_MESSAGE = "帮我写一个文案！大师" # starter启动时发送的消息
START_1_ICON = "copywriter.webp" # starter的图标，默认存放再icons下

# 一个prompt对应一个starter，第一个prompt_1为默认prompt
# 从第二个开始prompt_2对应stater的第一个prompt，必须和starter的数量对应
# 默认prompt：(prompt_1);starter：(prompt_2,prompt_3,prompt_4,prompt_5)最多四个
[PROMPTS]
PROMPT_1 = """
xxxxxx
"""

```

3. **同步环境**
    ```sh
    uv sync
    ```

4. **运行项目**
    ```sh
    cd src
    uv run -- chainlit run app.py -w --host 0.0.0.0 --port 8000
    ```
    - `--host` 和 `--port` 参数是可选的，可以根据需要进行调整，具体参考[chainlit](https://docs.chainlit.io/backend/command-line)

## Docker 部署 🐳

### docker
```shell
mv config.toml.exp config.toml
# 按需求修改.env
docker run -d -p 8000:8000 -v ./config.toml:/app/config.toml bitfennec/llmer:latest
```
访问 `http://localhost:8000` 查看正在运行的应用程序。

### docker-compose

```shell
git clone https://github.com/Mgrsc/llmer.git
cd llmer
```
根据需求编辑docker-compose.yaml
```yaml
services:
  llmer:
    image: bitfennec/llmer:latest
    container_name: llmer
    ports:
      - 30004:8000
    volumes:
      - ./config.toml:/app/config.toml
      # - ./icon:/app/icon # 可选，如需修改starter图标
      # - ./model:/app/model  # 可选，如需增加图标
```
```shell
docker-compose up -d
```

访问 `http://localhost:8000` 查看正在运行的应用程序。

## 贡献 🤝

如果你有任何改进建议或者想报告问题，欢迎提交 issue 或拉取请求（PR）。

## 许可证 📄

本项目基于 [Chainlit](https://github.com/Chainlit/Chainlit) 使用 Apache 2.0 许可证。详细信息请参阅 [LICENSE](./LICENSE) 文件。