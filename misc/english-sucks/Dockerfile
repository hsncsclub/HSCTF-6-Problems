FROM ubuntu

RUN apt-get update && apt-get install -y \
    xinetd \
 && rm -rf /var/lib/apt/lists/*

COPY ctf.xinetd /etc/xinetd.d/ctf

COPY mt flag.txt /

CMD ["xinetd", "-dontfork"]

EXPOSE 49151
