import discord
from discord.ext import commands

class Basic(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello, I am bot")

    # for events use
    # @commands.Cog.listener()

def setup(client):
    client.add_cog(Basic(client))