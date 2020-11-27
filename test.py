from Speech_Recognition import speech_recognizer
text = speech_recognizer.SpeechToText('path.wav')
print(text.recognize())
