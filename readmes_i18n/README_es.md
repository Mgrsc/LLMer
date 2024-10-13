# LLMER

Este proyecto te permite personalizar el Prompt de cada iniciador (starter), optimiza la interfaz de usuario con CSS y proporciona una imagen Docker para facilitar su implementación. Solo necesitas configurar config.json para que funcione de inmediato. A continuación se explica cómo configurar y ejecutar este proyecto.

## Índice 📚

- [Instalación y Configuración](#instalación-y-configuración)
- [Despliegue con Docker](#despliegue-con-docker)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Instalación y Configuración 🚀

1. **Instalar `uv`**
    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2. **Configurar config.toml**
```
[MODEL_MAP]
[[MODEL_MAP]."{name}"] # Corresponde a un modelo
profile_name = "Model A" # Nombre del modelo mostrado
model_name = "model-a" # Nombre real del modelo
markdown_description = "Descripción del Modelo A" # Descripción del modelo
icon = "/public/model/model-a.svg" # Ícono del modelo

# Configuración del starter, máximo cuatro starters
[STARTERS] 
START_1_LABEL = "Asistente de Redacción Profesional" # Contenido mostrado en la interfaz
START_1_MESSAGE = "¡Ayúdame a escribir un texto! Maestro" # Mensaje enviado al iniciar
START_1_ICON = "/public/icons/copywriter.webp" # Ícono del starter

# Un prompt corresponde a un starter, el primer prompt_1 es el prompt predeterminado
# A partir del segundo, prompt_2 corresponde al primer prompt del starter, debe coincidir con la cantidad de starters
# Prompt predeterminado: (prompt_1); starter: (prompt_2, prompt_3, prompt_4, prompt_5) máximo cuatro
[PROMPTS]
PROMPT_1 = """
xxxxxx
"""

```

3. **Sincronizar entorno**
    ```sh
    uv sync
    ```

4. **Ejecutar el proyecto**
    ```sh
    cd src
    uv run -- chainlit run app.py -w --host 0.0.0.0 --port 8000
    ```
    - Los parámetros `--host` y `--port` son opcionales y se pueden ajustar según sea necesario. Consulta [chainlit](https://docs.chainlit.io/backend/command-line) para más detalles.

## Despliegue con Docker 🐳

### docker
```shell
mv config.toml.exp config.toml
# Modifica .env según sea necesario
docker run -d -p 8000:8000 -v ./config.toml:/app/config.toml bitfennec/llmer:latest
```
Visita `http://localhost:8000` para ver la aplicación en ejecución.

### docker-compose

```shell
git clone https://github.com/Mgrsc/llmer.git
cd llmer
```
Edita docker-compose.yaml según sea necesario
```yaml
services:
  llmer:
    image: bitfennec/llmer:latest
    container_name: llmer
    ports:
      - 30004:8000
    volumes:
      - ./config.toml:/app/config.toml
      # - ./src/public/model:/app/src/public/model # Opcional, si necesitas agregar íconos
```
```shell
docker-compose up -d
```

Visita `http://localhost:8000` para ver la aplicación en ejecución.

## Contribución 🤝

Si tienes alguna sugerencia de mejora o deseas reportar un problema, no dudes en enviar un issue o un pull request (PR).

## Licencia 📄

Este proyecto se basa en [Chainlit](https://github.com/Chainlit/Chainlit) y utiliza la licencia Apache 2.0. Para más detalles, consulta el archivo [LICENSE](./LICENSE).