import time
import requests
import discord
from discord.ext import commands
import config


client = commands.Bot( command_prefix = config.BOT_PREFIX) #sets bot prefix.
client.remove_command('help') #removes a help command, you need to make help command yourself.


@client.event
async def on_ready(): #when bot connects to discord token.
    print('[+] Bot ready to work!')


@client.command()
async def hello(ctx):
    channel = ctx.message.channel #gets channel, where !hello command called.
    message_author = ctx.message.author #gets user, who called !hello command.

    await channel.send(f'{message_author.mention} Hello! Im Translate bot! Use !translate to translate your text.') #message_author.mention - pings user who called !hello command.


@client.command()
async def translate(ctx, *, text): # *, needs to make avaiable to write text with spaces.
    response = requests.get(f'https://t23.translatedict.com/1.php?p1=auto&p2=eng&p3={text}', json={ 'p1': 'auto', 'p2': 'eng', 'p3': text }) #doing request to translator api.
    translated = response.text #gets translated text from response.

    emb = discord.Embed(title='‹⚡› Translated:', colour=discord.Color.blue()) #creates a discord embed.
    emb.set_thumbnail(url="https://freepngimg.com/thumb/google/67088-tecnologia-play-google-icons-computer-translation-translate.png") #sets thumnail.
    emb.add_field(name= f'Translated Text:', value= f'```{translated}```')  #pushing translated text into embed.     
    await ctx.send(embed = emb) #sends it to channel, where command was called.



client.run(config.BOT_TOKEN) #runs a bot