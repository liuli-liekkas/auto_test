import socket


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(b'test', ('192.168.1.103', 8001))
    print('--end--')
    udp_socket.close()


if __name__ == '__main__':
    main()
