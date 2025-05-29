import selectors
import socket

sel = selectors.DefaultSelector()


def accept_connection(server_socket):
    client_socket, address = server_socket.accept()
    print(f"Подключен клиент: {address}")
    client_socket.setblocking(False)
    sel.register(client_socket, selectors.EVENT_READ, read_data)


def read_data(client_socket):
    try:
        data = client_socket.recv(1024)
        if data:
            print(f"[{client_socket.getpeername()}] Получено: {data.decode('utf-8')}")
            client_socket.sendall(f"Эхо: {data.decode('utf-8')}".encode('utf-8'))
        else:
            sel.unregister(client_socket)
            client_socket.close()
    except Exception as e:
        print(f"Ошибка: {e}")
        sel.unregister(client_socket)
        client_socket.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    server_socket.setblocking(False)
    sel.register(server_socket, selectors.EVENT_READ, accept_connection)
    print("Сервер с селекторами запущен на порту 12345...")

    while True:
        events = sel.select()
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == "__main__":
    start_server()