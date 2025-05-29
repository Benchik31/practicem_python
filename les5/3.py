import requests

response = requests.get("http://www.google.com")
print(f"Статус-код: {response.status_code}")

import requests
import time

start_time = time.time()
response = requests.get("http://www.google.com")
end_time = time.time()

print(f"Статус-код: {response.status_code}")
print(f"Тип содержимого: {response.headers.get('Content-Type')}")
print(f"Размер контента: {response.headers.get('Content-Length')} байт")
print(f"Время ответа: {end_time - start_time} секунд")

import socket

host = 'google.com'
port = 80

request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))

    s.sendall(request.encode())

    response = ""
    while True:
        part = s.recv(4096).decode()
        if not part:
            break
        response += part

headers, _, body = response.partition('\r\n\r\n')
status_line = headers.splitlines()[0]
status_code = status_line.split(' ')[1]

print(f"Статус-код: {status_code}")
print("Заголовки ответа:")
print('\n'.join(headers.splitlines()[1:]))