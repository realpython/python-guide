import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("My IP Address is :" + IPAddr)
