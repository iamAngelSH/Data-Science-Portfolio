# CORE STACK VERSION FOR ENVIRONMENT
FROM jupyter/pyspark-notebook:latest

# INSTALL NECESITIES FROM REQUIREMENTS.TXT FILE
COPY --chown=${NB_UID}:${NB_GID} requirements.txt /tmp/
RUN pip install --quiet --no-cache-dir --requirement /tmp/requirements.txt && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"