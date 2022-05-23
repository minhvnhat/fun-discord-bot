import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import asyncio

import os
from google.cloud import texttospeech
from google.cloud import texttospeech_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '.\\venv\discord-bot-349622-acc1834af7e3.json'
client = texttospeech_v1.TextToSpeechClient()

# config, no change
voice = texttospeech_v1.VoiceSelectionParams(
    language_code='vi-VN',
    name='vi-VN-Wavenet-A',
    ssml_gender=texttospeech_v1.SsmlVoiceGender.FEMALE,
)
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

async def request(text):
    # input text
    synthesis_input = texttospeech_v1.SynthesisInput(text=text)
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    with open("output.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')


class TTS(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client

    @commands.command(pass_context = True)
    async def tts(self, ctx):
        content = ctx.message.content[4:]
        await request(content)

        voice = ctx.voice_client
        source = FFmpegPCMAudio('output.mp3')
        voice.play(source)
        voice.pause()
        await asyncio.sleep(1)
        voice.resume()

    @tts.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()
        
def setup(client):
    client.add_cog(TTS(client))