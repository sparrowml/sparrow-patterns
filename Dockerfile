FROM python:3.9

ARG USER=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" && \
  echo $SNIPPET >> "/home/${USER}/.bashrc"

ENV LANG=C.UTF-8 \
  LC_ALL=C.UTF-8 \
  PATH="${PATH}:/root/.poetry/bin"

RUN apt update -y && apt install -y sudo
RUN groupadd --gid $USER_GID $USER && \
    useradd --uid $USER_UID --gid $USER_GID -m $USER && \
    echo ${USER} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USER} && \
    chmod 0440 /etc/sudoers.d/${USER} && \
    chsh ${USER} -s /bin/bash

RUN apt update -y
RUN DEBIAN_FRONTEND=noninteractive apt install -y tzdata
RUN apt install -y \
    build-essential \
    curl \
    git

USER ${USER}

CMD mkdir -p /code
WORKDIR /code
RUN mkdir sparrow_patterns && \
  touch sparrow_patterns/__init__.py
COPY setup.cfg .
COPY setup.py .
RUN pip install -U pip
RUN pip install -e .
ADD . .

ENTRYPOINT [ "make" ]