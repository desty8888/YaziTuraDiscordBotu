import discord
import random
sonuc = ["yazi", "tura"] 
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    elif message.content.startswith('!yazitura'):
        print(random.choice(sonuc))
        await message.channel.send(random.choice(sonuc))

client.run("TOKEN")