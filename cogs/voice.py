from discord.ext import commands
from discord import FFmpegPCMAudio
import asyncio

class Voice(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client

    @commands.command(pass_context = True)
    async def join(self, ctx):
        # if author is in a voice channel
        if (ctx.author.voice):
            # get the voice channel id
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
        else:
            await ctx.send("You're not in a voice channel!")

    @commands.command(pass_context = True)
    async def leave(self, ctx):
        # if the bot is in the voice channel
        if (ctx.voice_client):
            # disconnect
            await ctx.guild.voice_client.disconnect()
            await ctx.send("Left the voice channel")
        else:
            await ctx.send("I am not in a voice channel")

def setup(client):
    client.add_cog(Voice(client))