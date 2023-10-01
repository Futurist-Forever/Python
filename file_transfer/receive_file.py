import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12312

    sock.connect((host, port))
    sock.send(b"Hello server!")

    with open("Received_file", "wb") as out_file:
        print("File opened")
        print("Receiving data...")
        while True:
            if data := sock.recv(1024):
                out_file.write(data)

            else:
                break
    print("Successfully received the file")
    sock.close()
    print("Connection closed")


if __name__ == "__main__":
    main()
