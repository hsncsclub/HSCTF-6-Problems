FROM ubuntu

RUN apt-get update && apt-get install -y \
    python3 \
    xinetd \
 && rm -rf /var/lib/apt/lists/*

COPY ctf.xinetd /etc/xinetd.d/ctf

COPY repl.py flag.txt /

CMD ["xinetd", "-dontfork"]

EXPOSE 49151
