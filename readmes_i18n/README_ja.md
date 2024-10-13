# LLMER
このプロジェクトでは、各スターターのプロンプトをカスタマイズでき、CSSでUIを最適化し、Dockerイメージを提供して簡単にデプロイできます。config.jsonを設定するだけで、すぐに使用可能です。以下は、このプロジェクトの設定と実行方法の説明です。

## 目次 📚

- [インストールと設定](#インストールと設定)
- [Docker デプロイ](#docker-デプロイ)
- [貢献](#貢献)
- [ライセンス](#ライセンス)

## インストールと設定 🚀
1. **`uv`のインストール**
    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2. **config.tomlの設定**
```
[MODEL_MAP]
[[MODEL_MAP]."{name}"] # モデルに対応
profile_name = "Model A" # 表示されるモデル名
model_name = "model-a" # 実際のモデル名
markdown_description = "Description of Model A" # モデルの説明
icon = "/public/model/model-a.svg" # モデルのアイコン

# スターター設定、最大4つのスターター
[STARTERS] 
START_1_LABEL = "プロフェッショナルコピーライターアシスタント" # UIに表示される内容
START_1_MESSAGE = "コピーを書いてください！マスター" # スターター起動時に送信されるメッセージ
START_1_ICON = "/public/icons/copywriter.webp" # スターターのアイコン

# 1つのプロンプトが1つのスターターに対応、最初のprompt_1はデフォルトプロンプト
# 2つ目以降のprompt_2はスターターの最初のプロンプトに対応し、スターターの数と一致する必要がある
# デフォルトプロンプト：(prompt_1);スターター：(prompt_2,prompt_3,prompt_4,prompt_5)最大4つ
[PROMPTS]
PROMPT_1 = """
xxxxxx
"""

```

3. **環境の同期**
    ```sh
    uv sync
    ```

4. **プロジェクトの実行**
    ```sh
    cd src
    uv run -- chainlit run app.py -w --host 0.0.0.0 --port 8000
    ```
    - `--host` と `--port` パラメータはオプションで、必要に応じて調整可能です。詳細は[chainlit](https://docs.chainlit.io/backend/command-line)を参照してください。

## Docker デプロイ 🐳

### docker
```shell
mv config.toml.exp config.toml
# 必要に応じて.envを修正
docker run -d -p 8000:8000 -v ./config.toml:/app/config.toml bitfennec/llmer:latest
```
`http://localhost:8000` にアクセスして、実行中のアプリケーションを確認します。

### docker-compose

```shell
git clone https://github.com/Mgrsc/llmer.git
cd llmer
```
必要に応じてdocker-compose.yamlを編集
```yaml
services:
  llmer:
    image: bitfennec/llmer:latest
    container_name: llmer
    ports:
      - 30004:8000
    volumes:
      - ./config.toml:/app/config.toml
      # - ./src/public/model:/app/src/public/model # オプション、アイコンを追加する場合
```
```shell
docker-compose up -d
```

`http://localhost:8000` にアクセスして、実行中のアプリケーションを確認します。

## 貢献 🤝

改善提案や問題の報告があれば、issueやプルリクエスト（PR）を歓迎します。

## ライセンス 📄

このプロジェクトは[Chainlit](https://github.com/Chainlit/Chainlit)に基づいており、Apache 2.0ライセンスを使用しています。詳細は[LICENSE](./LICENSE)ファイルを参照してください。