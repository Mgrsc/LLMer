FROM ghcr.io/astral-sh/uv:bookworm-slim

LABEL maintainer="mgrsc <mail@occult.ac.cn>"

WORKDIR /app

COPY . /app

RUN uv sync --frozen

RUN sed -i 's|href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css"|href="/assets/katex.min.css"|' /app/.venv/lib/python3.12/site-packages/chainlit/frontend/dist/index.html

RUN mv /app/src/public/katex.min.css /app/.venv/lib/python3.12/site-packages/chainlit/frontend/dist/assets

WORKDIR /app/src

EXPOSE 8000

CMD ["uv", "run", "--", "chainlit", "run", "app.py", "--host", "0.0.0.0"]
