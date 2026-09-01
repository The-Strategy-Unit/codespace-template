FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Install uv during image build.
COPY --from=ghcr.io/astral-sh/uv:0.12.8 /uv /uvx /usr/local/bin/

ENV UV_LINK_MODE=copy