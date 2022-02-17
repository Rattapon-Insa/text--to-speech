from IPython.display import Audio
import gtts
from gtts import gTTS

def text_to_speech():
    gtts.lang.tts_langs(tld = 'com')
    tts = gTTS('hello', lang = 'en')
    tts.save('speech.mp3')



if __name__ == '__main__':
    input_text = input(" Your text here: ")
    text_to_speech()


