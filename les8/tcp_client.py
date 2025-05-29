import socket


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    message = input("Введите сообщение: ")
    client_socket.sendall(message.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print(f"Ответ от сервера: {response}")

    client_socket.close()


if __name__ == "__main__":
    start_client()