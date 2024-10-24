FROM ghcr.io/astral-sh/uv:bookworm-slim

RUN apt-get update && apt-get install -y tini

ENTRYPOINT ["/usr/bin/tini", "--"]

LABEL maintainer="mgrsc <mail@occult.ac.cn>"

WORKDIR /app

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV PATH="/app/.venv/bin:$PATH"

COPY . /app

RUN uv sync --frozen --no-dev

RUN sed -i 's|href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css"|href="/assets/katex.min.css"|' /app/.venv/lib/python3.12/site-packages/chainlit/frontend/dist/index.html

RUN mv /app/src/public/katex.min.css /app/.venv/lib/python3.12/site-packages/chainlit/frontend/dist/assets

WORKDIR /app/src

EXPOSE 8000

CMD ["chainlit", "run", "app.py", "--host", "0.0.0.0"]
