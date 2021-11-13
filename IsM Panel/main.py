import discord
import os
from discord.ext import commands
from models.Cheaker import *
import json

with open('config.json') as f:
	data = json.load(f)



client = commands.Bot(command_prefix=data['Perfix'])
client.remove_command('help')



print('---------------Cogs-------------------')
for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')
		print(f'{filename} Loaded')

print('---------------Models-------------------')
for filename in os.listdir('./models'):
	if filename.endswith('.py'):
		print(f'{filename} Loaded')


client.run(data['Token'])



