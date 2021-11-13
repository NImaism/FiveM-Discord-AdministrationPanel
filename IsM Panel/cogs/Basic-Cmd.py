from discord.ext import commands
import math
from discord.ext.commands import has_permissions

class Function(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	@has_permissions(administrator=True)
	async def ping(self, ctx):
		await ctx.send(f'**Ping Is {math.floor(self.client.latency * 10)}ms :white_check_mark: **')




def setup(client):
	client.add_cog(Function(client))

