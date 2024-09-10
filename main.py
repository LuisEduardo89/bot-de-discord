import random
import discord
from bot_logic import gen_pass
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
Bot = commands.Bot (command_prefix = "$" ,intents=intents)

@Bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {Bot.user}')

@Bot.command()
async def hello(ctx):
    await ctx.send("HI!")

@Bot.command()
async def bye(ctx):
    await ctx.send("😔")

@Bot.command()
async def Help(ctx):
    await ctx.send("$hello, $bye, $password, $help, $choose, $repeat")

@Bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@Bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))
    
@Bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

Bot.run("MTI3ODE1Nzg2NTI0ODYyNDY5MQ.GF1YYQ.HLdto7jN7sUeOYVzZvT3JUT3VPfuSoI7zcBKd0")
