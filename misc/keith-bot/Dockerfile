FROM python:3

RUN useradd -m ctf

WORKDIR /home/ctf

RUN cp -R /lib* /home/ctf && \
    cp -R /usr/lib* /home/ctf

RUN mkdir /home/ctf/dev && \
    mknod /home/ctf/dev/null c 1 3 && \
    mknod /home/ctf/dev/zero c 1 5 && \
    mknod /home/ctf/dev/random c 1 8 && \
    mknod /home/ctf/dev/urandom c 1 9 && \
    chmod 666 /home/ctf/dev/*

RUN pip3 install discord.py

COPY bot.py flag.txt /

ENV DISCORD_API_KEY=NTg0OTU3ODU4MzY2NjE5NjQ4.XPSerg.BMqTlYPbgd4_YnmqZDN6rgLxyU4

CMD python3 bot.py