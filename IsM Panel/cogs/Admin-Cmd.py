from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from models.Cheaker import *
from models.Writer import *


class Function(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	@has_permissions(administrator=True)
	async def start(self, ctx, resource):
		if cheakadmin(ctx.author.id):
			request(f"start {resource}")
			await ctx.send(f">>> Start Resource {resource} Has Ben Successful")

	@commands.command()
	@has_permissions(administrator=True)
	async def stop(self, ctx, resource):
		if cheakadmin(ctx.author.id):
			request(f"stop {resource}")
			await ctx.send(f">>> Stop Resource {resource}  Has Ben Successful")

	@commands.command()
	@has_permissions(administrator=True)
	async def weather(self, ctx, type):
		if cheakadmin(ctx.author.id):
			request(f"weather {type}")
			await ctx.send(f">>> Set Weather To {type}")
			await ctx.send(">>> Set Weather  Has Ben Successful")

	@commands.command()
	@has_permissions(administrator=True)
	async def time(self, ctx, h, m):
		if cheakadmin(ctx.author.id):
			request(f"time {h} {m}")
			await ctx.send(f">>> Set Time To {h}:{m}")
			await ctx.send(">>> Set Time  Has Ben Successful")

	@commands.command()
	@has_permissions(administrator=True)
	async def setperm(self, ctx, id, perm):
		if cheakadmin(ctx.author.id):
			request(f"setperm {id} {perm}")
			await ctx.send(f">>> Set Perm To {id} Level {perm}")
			await ctx.send(">>> Set Perm  Has Ben Successful")




def setup(client):
	client.add_cog(Function(client))
