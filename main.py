mport random
import discord
from bot_logic import gen_pass
from discord.ext import commands
from bot_logic import get_duck_image_url
import os 



# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
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
    await ctx.send("$hello, $bye, $password, $help, $elige, $rep")

@Bot.command()
async def cuenta(ctx):
    await ctx.send("1 2 3 4 5 6 7 8 9 10")

@Bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))
    
@Bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@Bot.command()
async def mem_random(ctx):
    mem_alet = random.choice(os.listdir("images"))
    
    with open(f'images/{mem_alet}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@Bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@Bot.command(description='For when you wanna settle the score some other way')
async def elige(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))
    
@Bot.command()
async def rep(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

Bot.run()
