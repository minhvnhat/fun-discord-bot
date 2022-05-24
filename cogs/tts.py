from discord.ext import commands
from discord import FFmpegPCMAudio
import asyncio
import os
from tempfile import TemporaryFile
from google.cloud import texttospeech
from google.cloud import texttospeech_v1
from dotenv import load_dotenv
load_dotenv()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('GOOGLE_CRED')
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
    fp = TemporaryFile()
    fp.write(response.audio_content)
    fp.seek(0)
    return fp


class TTS(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client

    @commands.command(pass_context = True)
    async def tts(self, ctx):
        content = ctx.message.content[4:]
        fp = await request(content)

        voice = ctx.voice_client
        source = FFmpegPCMAudio(fp, pipe=True)
        voice.play(source)
        voice.pause()
        await asyncio.sleep(1)
        voice.resume()

    @tts.before_invoke
    async def ensure_voice(self, ctx):
        # If bot not in any voice channel
        if ctx.voice_client is None:
            # If user is in a voice channel
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            # If user not in a voice channel
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        # If bot already in a voice channel
        else:
            # If bot and user arent in the same vc
            if ctx.voice_client.channel != ctx.author.voice.channel:
                await ctx.send('You need to be in my voicechannel.')
                raise commands.CommandInvokeError('You need to be in my voicechannel.')
            elif ctx.voice_client.is_playing():
                ctx.voice_client.stop()
        
def setup(client):
    client.add_cog(TTS(client))