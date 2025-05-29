import socket


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = input("Введите сообщение: ")
    client_socket.sendto(message.encode('utf-8'), ('localhost', 12345))

    response, _ = client_socket.recvfrom(1024)
    print(f"Ответ от сервера: {response.decode('utf-8')}")

    client_socket.close()


if __name__ == "__main__":
    start_client()