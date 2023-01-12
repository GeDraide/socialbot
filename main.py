# create feedback system
# create saving system. !Send saves to right chat!
# create correction system


import discord
import os
import openai
import json
# import random

openai.api_key = os.getenv('OPENAI_API_KEY')
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = "botty"
client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        if isinstance(message.channel, discord.channel.DMChannel):
            if not message.content.startswith('/'):
                return
        prompt = message.content
        response = openai.Completion.create(model='text-davinci-003', prompt=prompt, temperature=0.7, max_tokens=450)
        response = response['choices'][0]['text']
        # add the video creating AI.
        message.channel.send(response)
        with open('data.json', 'r') as f:
            data = json.load(f)
        if message.author.name not in data.keys():
            data.update({message.author.name: {}})
        data[message.author.name].update({message.content: response})
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)


client.run(TOKEN)
