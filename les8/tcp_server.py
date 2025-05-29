import socket


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)

    print("Сервер запущен на порту 12345...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Подключен клиент: {address}")

        data = client_socket.recv(1024).decode('utf-8')
        print(f"Получено сообщение: {data}")

        client_socket.sendall(f"Эхо: {data}".encode('utf-8'))

        client_socket.close()


if __name__ == "__main__":
    start_server()