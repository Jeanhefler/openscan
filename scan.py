import socket
IP = input("send a ip or domine: ")
ports = [80,443,21,22,53,23,8080]
for port in ports:
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.settimeout(0.5)
    code = client.connect_ex((IP,port))
    if code == 0:
        print(port,"open")