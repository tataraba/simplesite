FROM python:3.11
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update && apt-get install -y xdg-utils \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
EXPOSE 8000:8000
COPY . .

# Start the app
CMD uvicorn app.main:app --host 0.0.0.0 --port 8000