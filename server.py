import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
HEADER = 256

server = socket.socket()
server.bind((IP, PORT))
server.listen()
print(f"[LISTENING] El servidor esta esperando conexiones en {IP}")

conn, addr = server.accept()
print(f"[CONNECTED] Nueva conexion en {addr}")

while True:
  
  msg = conn.recv(1024).decode("utf-8")
  print(f"[CLIENT] El cliente dice: {msg}")
  conn.send("RECIBIDO".encode("utf-8"))
  msg_len = conn.recv(HEADER).decode("utf-8")
  msg = conn.recv(int(msg_len)).decode("utf-8")
