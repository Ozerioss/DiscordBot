import discord

client = discord.Client() #establish connection to the client
token = "Rnfg2vYBYS_EvDBKbqudR3BDJRoSpmja"
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
        await client.send_message(message.channel, "Sup homie")

client.run(token)


