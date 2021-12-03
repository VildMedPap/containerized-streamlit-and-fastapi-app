# Dockerized Streamlit App

This is just a simple dockerized streamlit setup. From here, you can built in your own app and take advantage of containerization.

## Quick start

Build the image

```sh
docker build -t streamlitapp .
```

Run the container

```sh
docker run -p 8501:8501 streamlitapp:latest
```

In your browser, attend 127.0.0.1:8501 and see the streamlit app alive

## Docker setup

The `Dockerfile` is a multistage file which uses the `python:3.8` image for building dependencies and the `python:3.8-slim` image for sourcing the app. The final image size is `505MB`.
