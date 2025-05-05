import socket
import json

HOST = '0.0.0.0'
PORT = 8080

def handle_request(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    print(f"received request:\n{request}")

    response_body = json.dumps({"message": "Hello Server Python", "status": "success"})

    response_headers = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: application/json\r\n"
        f"Content-Length: {len(response_body)}\r\n"
        "Connection: close\r\n"
        "\r\n"
    )

    response = response_headers + response_body
    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()


def create_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print(f"Server is running at http://{HOST}:{PORT}")

        while True:
            client_socket, address = server_socket.accept()
            print(f"Connection from {address}")
            handle_request(client_socket)

if __name__ == "__main__":
    create_server()