from datetime import datetime
import socket
import datetime

IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
HEADER = 256
header = {
    "to": IP,
    "from": IP,
    "data_length": 0,
    "timestamp": 0,
}

client = socket.socket()
client.connect((IP, PORT))
print(f"[CONNECTED] Conectado al servidor en {IP}")

while True:
  
  client.send(input("Ingrese un mensaje: ").encode("utf-8"))
  msg = client.recv(1024).decode("utf-8")
  print(f"[SERVER] Servidor dice: {msg}")
  msg = input(" ")
  msg_len = len(msg)
  header["data_length"] = msg_len
  header["timestamp"] = datetime.datetime.now()
  head = str(header)
  msg_len += " "*(HEADER - len(msg_len))
  client.send(msg_len.encode("utf-8"))

