from Speech_Recognition import speech_recognizer
import socket


class Server:
    def __init__(self):
        pass

    def receive_file(self):
        pass


serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', 53210))

while True:
    file = open('Sound1.wav', 'wb')
    serv_sock.listen(10)
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)
    data = client_sock.recv(1024)
    while data:
        file.write(data)
        data = client_sock.recv(1024)
    file.close()

    text = speech_recognizer.SpeechToText('Sound1.wav')
    print(text.recognize())
    client_sock.close()
