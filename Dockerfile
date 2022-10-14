FROM python:3.9

ARG USERNAME=kevin
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ENV LANG=C.UTF-8 \
  LC_ALL=C.UTF-8 \
  PATH="${PATH}:/root/.poetry/bin"

RUN apt update -y && apt install -y sudo
RUN groupadd --gid $USER_GID $USERNAME &&\
 useradd --uid $USER_UID --gid $USER_GID -m $USERNAME &&\  
 echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} &&\
 chmod 0440 /etc/sudoers.d/${USERNAME}

RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" && echo $SNIPPET >> "/home/${USERNAME}/.bashrc"

RUN apt update -y
RUN DEBIAN_FRONTEND=noninteractive apt install -y tzdata
RUN apt install -y \
    build-essential \
    curl \
    git

USER ${USERNAME}

CMD mkdir -p /code
WORKDIR /code
RUN mkdir sparrow_patterns && \
  touch sparrow_patterns/__init__.py
COPY setup.cfg .
COPY setup.py .
RUN pip install -e . --user
ADD . .

ENTRYPOINT [ "make" ]