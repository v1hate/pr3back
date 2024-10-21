import socket
import os

HOST = '0.0.0.0'
PORT = 5001
UPLOAD_FOLDER = 'app/uploads/'

def start_tcp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Servidor TCP escuchando en {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()
            print(f"Conexión desde {addr}")

            filename = conn.recv(1024).decode()
            filepath = os.path.join(UPLOAD_FOLDER, filename)

            with open(filepath, 'wb') as f:
                while True:
                    data = conn.recv(4096)
                    if not data:
                        break
                    f.write(data)

            print(f"Archivo {filename} recibido.")
            conn.close()

if __name__ == "__main__":
    start_tcp_server()
