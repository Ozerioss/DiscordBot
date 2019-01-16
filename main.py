import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio

client = discord.Client() #establish connection to the client
token = "NDQwNDE0MTQ3NTYyMTc2NTIy.Dx9iMg.POAiu18RRMzXOlhIFdSBoLxq3gE"

@client.event
async def on_ready():
    print("The bot is ready !")
    await client.change_presence(game = discord.Game(name = "Thomas is a bitch"))

@client.event
async def on_message(message):
    #To avoid infinite loops where the bot talks to itself
    if(message.author == client.user):
        return
    if(message.content == "**"):
        await client.send_message(message.channel, ".play smth")
        await client.send_message(message.channel, "alright alright alright")


#Todo : add the bot to the channel and try to communicate with the other bot
""" @Bot.command(pass_context = True)
async def join(ctx):
    author = ctx.message.author
    channel = author.voice_channel
    await bot.join_voice_channel(channel) """

client.run(token)


