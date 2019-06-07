import asyncio
from discord.ext import commands
import os

bot = commands.Bot(command_prefix=commands.when_mentioned_or("_"))
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Logged in as", bot.user)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.guild is None:
        await bot.process_commands(message)
    elif bot.user in message.mentions:
        await message.channel.send(f"{message.author.mention} DM me")

@bot.command(name="eval")
async def _eval(ctx, *, body):
    if body.startswith("```") and body.endswith("```"):
        body = "\n".join(body.split("\n")[1:-1])
    else:
        body = body.strip("` \n")

    process = await asyncio.create_subprocess_exec("env", "-i", "python3", "eval.py", stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

    try:
        out, err = await asyncio.wait_for(process.communicate(body.encode()), 5)
    except asyncio.TimeoutError:
        await process.kill()
    else:
        if out or err:
            await ctx.send(f"```py\n{out.decode()}{err.decode()}\n```")

bot.run(os.environ["DISCORD_API_KEY"], reconnect=True)
