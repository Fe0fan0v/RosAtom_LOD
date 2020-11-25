from vosk import Model, KaldiRecognizer
import os, wave, json


class SpeechToText:
    def __init__(self, file_folder):
        self.file_folder = file_folder

    def recognize(self):
        if not os.path.exists("Speech_Recognition/model"):
            print(
                "Please create speech model as 'model' in the current folder.")
            exit(1)

        wf = wave.open(self.file_folder, "rb")
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
            print("Audio file must be WAV format mono PCM.")
            exit(1)

        model = Model("Speech_Recognition/model")
        rec = KaldiRecognizer(model, wf.getframerate())
        result = ''

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                x = json.loads(rec.Result())
                result += x['text'] + ' '
            else:
                pass
        result += json.loads(rec.FinalResult())['text']

        return result