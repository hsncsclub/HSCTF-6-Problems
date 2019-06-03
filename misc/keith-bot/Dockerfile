FROM python:3

RUN pip3 install discord.py

COPY forever.py bot.py flag.txt /

ENV DISCORD_API_KEY=NTg0OTU3ODU4MzY2NjE5NjQ4.XPSerg.BMqTlYPbgd4_YnmqZDN6rgLxyU4

CMD ./forever.py bot.py