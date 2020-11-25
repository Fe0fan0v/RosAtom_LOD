from Speech_Recognition import speech_recognizer

text = speech_recognizer.SpeechToText('Speech_Recognition/speech_examples/Sound1.wav')
print(text.recognize())