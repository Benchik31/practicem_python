import socket
import threading


def handle_client(client_socket, address):
    try:
        data = client_socket.recv(1024).decode('utf-8')
        print(f"[{address}] Получено: {data}")
        client_socket.sendall(f"Эхо: {data}".encode('utf-8'))
    except Exception as e:
        print(f"Ошибка при обработке клиента {address}: {e}")
    finally:
        client_socket.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Многопоточный сервер запущен на порту 12345...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Подключен клиент: {address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()


if __name__ == "__main__":
    start_server()