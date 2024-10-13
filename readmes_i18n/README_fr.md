# LLMER

Ce projet vous permet de personnaliser le Prompt de chaque starter, optimise l'interface utilisateur avec CSS, et fournit une image Docker pour un déploiement facile. Il suffit de configurer config.json pour une utilisation immédiate. Voici les instructions pour configurer et exécuter ce projet.

## Sommaire 📚

- [Installation et configuration](#installation-et-configuration)
- [Déploiement Docker](#déploiement-docker)
- [Contribution](#contribution)
- [Licence](#licence)

## Installation et configuration 🚀

1. **Installer `uv`**
   ```sh
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Configurer config.toml**
   ```
   [MODEL_MAP]
   [[MODEL_MAP]."{name}"] # Correspond à un modèle
   profile_name = "Model A" # Nom du modèle affiché
   model_name = "model-a" # Nom réel du modèle
   markdown_description = "Description of Model A" # Description du modèle
   icon = "/public/model/model-a.svg" # Icône du modèle

   # Configuration des starters, jusqu'à quatre starters
   [STARTERS] 
   START_1_LABEL = "Assistant de rédaction professionnel" # Contenu affiché du starter
   START_1_MESSAGE = "Aidez-moi à rédiger un texte ! Maître" # Message envoyé au démarrage du starter
   START_1_ICON = "/public/icons/copywriter.webp" # Icône du starter

   # Un prompt correspond à un starter, le premier prompt_1 est le prompt par défaut
   # À partir du deuxième, prompt_2 correspond au premier prompt du starter, doit correspondre au nombre de starters
   # Prompt par défaut : (prompt_1); starter : (prompt_2, prompt_3, prompt_4, prompt_5) jusqu'à quatre
   [PROMPTS]
   PROMPT_1 = """
   xxxxxx
   """
   ```

3. **Synchroniser l'environnement**
   ```sh
   uv sync
   ```

4. **Exécuter le projet**
   ```sh
   cd src
   uv run -- chainlit run app.py -w --host 0.0.0.0 --port 8000
   ```
   - Les paramètres `--host` et `--port` sont optionnels et peuvent être ajustés selon les besoins, voir [chainlit](https://docs.chainlit.io/backend/command-line) pour plus de détails.

## Déploiement Docker 🐳

### docker
```shell
mv config.toml.exp config.toml
# Modifier .env selon les besoins
docker run -d -p 8000:8000 -v ./config.toml:/app/config.toml bitfennec/llmer:latest
```
Accédez à `http://localhost:8000` pour voir l'application en cours d'exécution.

### docker-compose

```shell
git clone https://github.com/Mgrsc/llmer.git
cd llmer
```
Modifier docker-compose.yaml selon les besoins
```yaml
services:
  llmer:
    image: bitfennec/llmer:latest
    container_name: llmer
    ports:
      - 30004:8000
    volumes:
      - ./config.toml:/app/config.toml
      # - ./src/public/model:/app/src/public/model # Optionnel, pour ajouter des icônes
```
```shell
docker-compose up -d
```

Accédez à `http://localhost:8000` pour voir l'application en cours d'exécution.

## Contribution 🤝

Si vous avez des suggestions d'amélioration ou souhaitez signaler un problème, n'hésitez pas à soumettre un issue ou une pull request (PR).

## Licence 📄

Ce projet est basé sur [Chainlit](https://github.com/Chainlit/Chainlit) sous licence Apache 2.0. Pour plus de détails, consultez le fichier [LICENSE](./LICENSE).