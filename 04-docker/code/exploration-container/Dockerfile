FROM python:3.8.19-alpine3.18
MAINTAINER Quinn Snyder <qsnyder@cisco.com>

COPY requirements.txt . 

ENV info "DNE-BASE v3.7.6: Python 3.7.6, Ansible 2.9.5, Openconnect, VIRLUtils"

RUN echo 'PS1="\[\e[36m\]\u\[\e[m\]\[\e[37m\]@\[\e[m\]\[\e[32m\]dnebase376\[\e[m\]:\[\e[33m\]\w\[\e[m\]\[\e[33m\]\\$\[\e[m\] "' >> /root/.bashrc 

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories && \
    apk update && \
    apk add --no-cache make curl bash git openssh gcc linux-headers musl-dev libffi-dev openssl-dev libxml2-dev libxslt-dev wget openconnect && \
    python -m ensurepip && \
    pip install --upgrade pip setuptools && \
    rm -r /root/.cache && \
    pip install -r requirements.txt && \
    rm -rf /var/cache/apk/*
WORKDIR "/mycode" 
CMD ["/bin/bash"]
