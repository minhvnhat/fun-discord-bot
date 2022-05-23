import os
from google.cloud import texttospeech
from google.cloud import texttospeech_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '.\\venv\discord-bot-349622-acc1834af7e3.json' 
client = texttospeech_v1.TextToSpeechClient()

text = "ái chà bạn đã làm tôi mở mang"

# input text
synthesis_input = texttospeech_v1.SynthesisInput(text=text)

voice = texttospeech_v1.VoiceSelectionParams(
    language_code='vi-VN',
    name='vi-VN-Wavenet-A',
    ssml_gender=texttospeech_v1.SsmlVoiceGender.FEMALE,
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')