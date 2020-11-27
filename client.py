import socket


client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('127.0.0.1', 53210))

file = open('Speech_Recognition/speech_examples/Sound1.wav', 'rb')
line = file.read(1024)
while line:
    client_sock.send(line)
    line = file.read(1024)
file.close()
client_sock.close()
print('Had sent')
