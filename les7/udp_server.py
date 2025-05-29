import socket


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))
    print("UDP сервер запущен на порту 12345...")

    while True:
        data, address = server_socket.recvfrom(1024)
        print(f"[{address}] Получено: {data.decode('utf-8')}")
        server_socket.sendto(f"Эхо: {data.decode('utf-8')}".encode('utf-8'), address)


if __name__ == "__main__":
    start_server()