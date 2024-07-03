FROM ubuntu:22.04
WORKDIR /workspace

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apt-get update && apt-get install -y \
    sudo wget git python3 python3-pip \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd --gid ${USER_GID} ${USERNAME} \
    && useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} \
    && echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME}

RUN apt-get update && apt-get install -y python3 python3-pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN gunicorn --version

RUN apt-get update && apt-get install -y mysql-client

COPY ./apps /workspace/apps

ENV PYTHONPATH "${PYTHONPATH}:/workspace"
