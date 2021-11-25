import socket
import datetime

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    sock.bind(('', 80))
    print("Using port 80")
except OSError:
    sock.bind(('', 8080))
    print("Using port 8080")

with open("1.html", "r") as file:
  html1 = file.read()

with open("2.html", "r") as file:
  html2 = file.read()

with open("index.html", "r") as file:
  index = file.read()

sock.listen(5)


conn, addr = sock.accept()
print("Connected", addr)

data = conn.recv(8192)
msg = data.decode()

print(msg)

if "1.html" in msg:
    ChosenFile = html1
elif "2.html" in msg:
    ChosenFile = html2
else:
    ChosenFile = index

now = datetime.datetime.now()


resp = f"""HTTP/1.1 200 OK
Date: {now.strftime("%a, %d %b %Y %H:%M:%S")}
Server: SelfMadeServer v0.0.1
Content-Length: {len(ChosenFile)}
Content-Type: text/html
Connection: close

{ChosenFile}"""

print(resp)
conn.send(resp.encode())

conn.close()