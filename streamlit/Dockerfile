# STAGE: Build ----------------------------------------------------------------
# In this stage we build the foundation of the final image. We compile the
# libraries needed for the model.
# --------------------------------------------------------------------- (BEGIN)
FROM python:3.8 AS build
WORKDIR /setup
COPY requirements.txt requirements.txt
RUN pip install --user --no-cache-dir --no-warn-script-location -r requirements.txt
# ----------------------------------------------------------------------- (END)


# STAGE: Source ---------------------------------------------------------------
# In this stage we copy the compiled libraries from the build stage and we copy
# the source files.
# --------------------------------------------------------------------- (BEGIN)
FROM python:3.8-slim AS source
ENV PATH=/root/.local/bin:$PATH
WORKDIR /app
COPY --from=build /root/.local /root/.local
COPY . .
# ----------------------------------------------------------------------- (END)


# STAGE: Production -----------------------------------------------------------
# This stage is built upon the source stage. In this stage we launch the app.
# --------------------------------------------------------------------- (BEGIN)
FROM source AS production
EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]
# ----------------------------------------------------------------------- (END)
