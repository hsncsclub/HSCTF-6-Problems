FROM ubuntu

RUN apt-get update && apt-get install -y \
    python \
    xinetd \
 && rm -rf /var/lib/apt/lists/*

COPY ctf.xinetd /etc/xinetd.d/ctf

COPY problem.py secret.py flag.txt /

CMD ["xinetd", "-dontfork"]

EXPOSE 49151
