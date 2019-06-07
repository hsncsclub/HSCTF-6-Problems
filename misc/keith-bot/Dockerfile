FROM python:alpine

RUN pip install discord.py

COPY bot.py eval.py /
COPY flag.txt /home

ENV DISCORD_API_KEY=NTg0OTU3ODU4MzY2NjE5NjQ4.XPSerg.BMqTlYPbgd4_YnmqZDN6rgLxyU4

CMD python3 bot.py
