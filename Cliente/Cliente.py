import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("192.168.60.1", 5002))
    print(s)
    s.sendall(b"Ola, mundo")
    dados = s.recv(1024)
    print(f"Resposta do servidor: {dados.decode()}")