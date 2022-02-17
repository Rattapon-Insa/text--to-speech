
from gtts import gTTS
import subprocess


def text_to_speech():
    with open('text_input.txt') as f:
        lines = f.read()
    tts = gTTS(lines, lang = 'th')
    tts.save('speech.mp3')
    file = 'speech.mp3'
    subprocess.call(["afplay", file])



if __name__ == '__main__':
    text_to_speech()


