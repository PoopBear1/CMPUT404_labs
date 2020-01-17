import socket,sys

def create_tcp_socket():
    print('Creating socket')
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except(s.error,msg):
        print(f'Failed to create socket. Error code: {str(msg[0])},Erro message: {msg[1]}')
        sys.exit()
    print('Socket created successfully')
    return s


def get_remote_ip(host):
    print(f'getting IP for{host}')
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print('Host could not be resolved,exting')
        sys.exit()
    print(f'IP address of {host} is {remote_ip}')
    return remote_ip

def send_data(serversocket,payload):
    print('Sending payload')
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        print('Send failed')
        sys.exit()
    print("Payload sent successfully")

def main():
    host = "www.google.com"
    port =  80
    payload = f'Get/ HTTP/1.0\R\nHost: {host} \r\n\r\n'
    buffer_size=4096

    s = create_tcp_socket()

    remote_ip = get_remote_ip(host)

    s.connect((remote_ip,port))

    print(f'Socket Connected to {host} on ip {remote_ip}')

    send_data(s,payload)
    s.shutdown(socket.SHUT_WR)

    full_data = b"" 
    while True:
        data = s.recv(buffer_size)


if __name__ == "__main__":
    main()