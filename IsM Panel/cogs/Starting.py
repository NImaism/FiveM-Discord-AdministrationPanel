import discord
from discord.ext import commands, tasks
from itertools import cycle
import json

class Function(commands.Cog):

	def __init__(self, client):
		self.client = client
		with open('config.json') as f:
			data = json.load(f)

		self.status = cycle(data["Status"])


	@tasks.loop(seconds=15)
	async def change_status(self):
		await self.client.change_presence(activity=discord.Game(next(self.status)))

	@commands.Cog.listener()
	async def on_ready(self):
		print('----------------Status------------------')
		print(f"Logged in as {self.client.user.name}")
		print(f"Discord.py API version : {discord.__version__}")
		print('All Checked Successful')
		print('Develop By NImaism#4092')
		print('---------------Logger-------------------')
		self.change_status.start()

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.CommandNotFound):
			cmdn = discord.Embed(
				title="Not Found",
				description="Cmd Not Found",
				colour=0x00FFF8
			)
			await ctx.send(embed=cmdn)


	@commands.Cog.listener()
	async def on_message(self, message):
		if isinstance(message.channel, discord.channel.DMChannel) and message.author != self.client.user:
			await message.channel.send(">>> **Sorry, But I Dont Process Commands On Direct Messages...**")



def setup(client):
	client.add_cog(Function(client))
