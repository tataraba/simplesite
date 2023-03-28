# Create a Dockerfile that pulls python 3.11 and installs the requirements

ARG IMAGE=bullseye

FROM --platform=amd64 mcr.microsoft.com/devcontainers/${IMAGE}
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update && apt-get install -y xdg-utils \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip