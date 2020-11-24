import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}. Welcome to Io.'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

client.run("secret")