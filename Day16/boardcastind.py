from gtts import gTTS

text = "도움필요하시면 말씀해주세요"
tts = gTTS(text, lang='ko')
tts.save('result.mp3')