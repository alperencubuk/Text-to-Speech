from gtts import gTTS

def text_to_speech(input_name, output_name, language):
    file = open(input_name, 'r')
    content = file.read()
    file.close()
    sound = gTTS(text=content, lang=language)
    sound.save(output_name + '.mp3')
	#https://pypi.org/project/gTTS/
	
text_to_speech('input_en.txt', 'sound_en', 'en')
#text_to_speech('input_tr.txt', 'sound_tr', 'tr')

print('Done!')