{% if gpu %}FROM nvidia/cuda:11.3.1-cudnn8-runtime-ubuntu20.04{% else %}FROM python:3.9{% endif %}

ARG USER=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID{% if gpu %}

RUN apt-key adv --fetch-keys https://developer.download.nvidia.cn/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub{% endif %}

RUN apt update -y && apt install -y sudo
RUN groupadd --gid $USER_GID $USER && \
    useradd --uid $USER_UID --gid $USER_GID -m $USER && \
    echo ${USER} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USER} && \
    chmod 0440 /etc/sudoers.d/${USER} && \
    chsh ${USER} -s /bin/bash

RUN mkdir -p /commandhistory
RUN chown -R ${USER} /commandhistory

RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" && \
  echo $SNIPPET >> "/home/${USER}/.bashrc"

RUN apt update -y
RUN DEBIAN_FRONTEND=noninteractive apt install -y tzdata
RUN apt install -y \
    build-essential \
    curl \
    git{% if gpu %}

# GPU Setup
RUN apt-get install -y \
    libcairo2-dev \
    libgl1-mesa-glx \
    software-properties-common

# Install Python 3.9
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install -y python3.9-dev python3.9-venv
RUN python3.9 -m ensurepip
RUN ln -s /usr/bin/python3.9 /usr/local/bin/python
RUN ln -s /usr/local/bin/pip3.9 /usr/local/bin/pip
RUN pip install --upgrade pip

ENV PIP_EXTRA_INDEX_URL https://download.pytorch.org/whl/cu113{% endif %}

RUN mkdir -p /code
RUN chown -R ${USER} /code
WORKDIR /code

USER ${USER}
ENV PATH "${PATH}:/home/${USER}/.local/bin"

RUN mkdir {{ source_directory }} && \
  touch {{ source_directory }}/__init__.py
COPY setup.cfg .
COPY setup.py .
RUN pip install -U pip
RUN pip install -e .
ADD . .

ENTRYPOINT [ "make" ]
