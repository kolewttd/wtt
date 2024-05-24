import socket

# Create a raw socket
sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

# Bind the socket to an IP address and port
sock.bind(('localhost', 12345))

# Send plaintext data
sock.sendto(b'Hello World', ('localhost', 54321))

# Receive plaintext data
data, addr = sock.recvfrom(1024)
print(data.decode())
