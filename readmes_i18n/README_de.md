# LLMER

Dieses Projekt ermöglicht es Ihnen, den Prompt jedes Starters anzupassen, optimiert die Benutzeroberfläche mit CSS und bietet ein Docker-Image für eine einfache Bereitstellung. Sie müssen nur die config.json konfigurieren, um es sofort einsatzbereit zu machen. Im Folgenden finden Sie Anweisungen zur Einrichtung und Ausführung dieses Projekts.

## Inhaltsverzeichnis 📚

- [Installation und Konfiguration](#installation-und-konfiguration)
- [Docker-Bereitstellung](#docker-bereitstellung)
- [Beitrag](#beitrag)
- [Lizenz](#lizenz)

## Installation und Konfiguration 🚀

1. **Installation von `uv`**
   ```sh
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Konfiguration der config.toml**
   ```
   [MODEL_MAP]
   [[MODEL_MAP]."{name}"] # Entspricht einem Modell
   profile_name = "Model A" # Angezeigter Modellname
   model_name = "model-a" # Tatsächlicher Modellname
   markdown_description = "Beschreibung von Model A" # Modellbeschreibung
   icon = "/public/model/model-a.svg" # Modell-Icon

   # Starter-Einstellungen, maximal vier Starter
   [STARTERS] 
   START_1_LABEL = "Professioneller Textassistent" # Inhalt, der im UI angezeigt wird
   START_1_MESSAGE = "Schreib mir einen Text! Meister" # Nachricht beim Starten des Starters
   START_1_ICON = "/public/icons/copywriter.webp" # Icon des Starters

   # Ein Prompt entspricht einem Starter, der erste prompt_1 ist der Standard-Prompt
   # Ab dem zweiten prompt_2 entspricht der erste Prompt des Starters, muss mit der Anzahl der Starter übereinstimmen
   # Standard-Prompt: (prompt_1); Starter: (prompt_2, prompt_3, prompt_4, prompt_5) maximal vier
   [PROMPTS]
   PROMPT_1 = """
   xxxxxx
   """
   ```

3. **Umgebung synchronisieren**
   ```sh
   uv sync
   ```

4. **Projekt ausführen**
   ```sh
   cd src
   uv run -- chainlit run app.py -w --host 0.0.0.0 --port 8000
   ```
   - Die Parameter `--host` und `--port` sind optional und können nach Bedarf angepasst werden. Weitere Informationen finden Sie unter [chainlit](https://docs.chainlit.io/backend/command-line).

## Docker-Bereitstellung 🐳

### docker
```shell
mv config.toml.exp config.toml
# .env nach Bedarf ändern
docker run -d -p 8000:8000 -v ./config.toml:/app/config.toml bitfennec/llmer:latest
```
Besuchen Sie `http://localhost:8000`, um die laufende Anwendung anzuzeigen.

### docker-compose

```shell
git clone https://github.com/Mgrsc/llmer.git
cd llmer
```
Bearbeiten Sie docker-compose.yaml nach Bedarf
```yaml
services:
  llmer:
    image: bitfennec/llmer:latest
    container_name: llmer
    ports:
      - 30004:8000
    volumes:
      - ./config.toml:/app/config.toml
      # - ./src/public/model:/app/src/public/model # Optional, falls Icons hinzugefügt werden sollen
```
```shell
docker-compose up -d
```

Besuchen Sie `http://localhost:8000`, um die laufende Anwendung anzuzeigen.

## Beitrag 🤝

Wenn Sie Verbesserungsvorschläge haben oder ein Problem melden möchten, sind Sie herzlich eingeladen, ein Issue oder Pull Request (PR) einzureichen.

## Lizenz 📄

Dieses Projekt basiert auf [Chainlit](https://github.com/Chainlit/Chainlit) und verwendet die Apache 2.0-Lizenz. Weitere Informationen finden Sie in der [LICENSE](./LICENSE)-Datei.