import discord
from discord.ext import commands
import os
import sys
import inspect
import io
import textwrap
import traceback
from contextlib import redirect_stdout

bot = commands.Bot(command_prefix=commands.when_mentioned_or('_'))
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Logged in as " + str(bot.user))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.guild is None:
        await bot.process_commands(message)

@bot.command(name='eval')
async def _eval(ctx, *, body):
    env = {'__builtins__': {}}
    body = cleanup_code(body)
    stdout = io.StringIO()
    err = out = None

    to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

    try:
        exec(to_compile, env)
    except Exception as e:
        err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
        return

    func = env['func']
    try:
        with redirect_stdout(stdout):
            ret = await func()
    except Exception as e:
        value = stdout.getvalue()
        err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
    else:
        value = stdout.getvalue()
        if ret is None:
            if value:
                out = await ctx.send(f'```py\n{value}\n```')
        else:
            bot._last_result = ret
            out = await ctx.send(f'```py\n{value}{ret}\n```')

def cleanup_code(content):
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    return content.strip('` \n')

def get_syntax_error(e):
    if e.text is None:
        return f'```py\n{e.__class__.__name__}: {e}\n```'
    return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'

bot.run(os.environ.get("DISCORD_API_KEY"), reconnect=True)
