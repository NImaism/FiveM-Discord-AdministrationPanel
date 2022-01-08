import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord_components import *
from models.Fivem import *
from models.Cheaker import *
from models.Writer import *


class Function(commands.Cog):

    def __init__(self, client):
        self.client = client
        DiscordComponents(client)

    @commands.command()
    @has_permissions(administrator=True)
    async def panel(self, ctx):
        PanelMouadel = discord.Embed(
            title="Server Status",
            url=cheaklink(ctx.author.id),
            description="",
            colour=0x00FF36
        )
        PanelMouadel.add_field(name="Owner", value=cheakowner(ctx.author.id), inline=False)
        PanelMouadel.add_field(name="Players", value=cheakcount(cheakip(ctx.author.id)), inline=False)
        PanelMouadel.add_field(name="Server Build", value=cheakbuild(cheakip(ctx.author.id)), inline=False)
        PanelMouadel.set_footer(text="Develop By IsM Company")
        PanelMouadel.set_image(url=cheakbanner(cheakip(ctx.author.id)))
        Help = discord.Embed(
            title="Help Commands",
            description="",
            colour=0x00FF36
        )
        Help.add_field(name="start", value='start ResourceName', inline=False)
        Help.add_field(name="stop", value='stop ResourceName', inline=False)
        Help.add_field(name="setperm", value='setperm id level', inline=False)
        Help.add_field(name="time", value='time Hours Minutes', inline=True)
        Help.add_field(name="weather", value='weather type', inline=True)
        Help.set_footer(text="Develop By IsM Company")
        Help.set_image(url=cheakbanner(cheakip(ctx.author.id)))
        await ctx.send(
            embed=PanelMouadel,
            components=[
                Button(label="Help", custom_id="button2", style=3)
            ]
        )
        while True:
            response = await self.client.wait_for("button_click")
            if response.channel == ctx.channel and response.author.id == ctx.author.id:
                if response.component.label == 'Help':
                    await response.send(embed=Help)


def setup(client):
    client.add_cog(Function(client))



