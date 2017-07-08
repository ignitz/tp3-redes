#!/usr/bin/python3
from utils import *

class Client:
    """docstring for Client."""
    def __init__(self, host, port):
        print_warning('Client instanced')
        self.host = host
        self.port = int(port) if not isinstance(port, int) else port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

    def __del__(self):
        print_blue('Client died')
        self.sock.close()

    def send_data(self):
        # sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        pass

    def receive_data(self):
        pass

    def get_command(self):
        command = sys.stdin.readline()
        if command[:-1] == 'help':
            # TODO: completar com português correto
            print_blue('query: Faz consulta')
            print_blue('quit: Fecha o cliente')
            print()
        elif command[:-1] == 'query':
            # TODO: Query com o server, não esquecer o timeout
            pass
        elif command[:-1] == 'quit':
            sys.exit()
        else:
            print_error('Unknow command ' + str(command))

    def start(self):
        # NOTE: Tem que criar um port de escuta pra testar no localhost
        self.sock.bind((self.host, self.port))

        # Clear terminal
        print('\033c', end="")
        print_blue('Type "help" for more info!')

        while True:
            socket_list = [sys.stdin, self.sock]

            # stuck in here until a fd is ready
            try:
                read_sockets, write_sockets, error_sockets = select.select(socket_list,[],[])
            except Exception as e:
                print_error('Something wrong in select')
                print_error(socket_list)
                sys.exit()

            for sock in read_sockets:
                if sock == self.sock:
                    print_warning('Receive data')
                    # TODO: Receive data
                elif sock == sys.stdin:
                    self.get_command()
                else:
                    print_error('Unexpected state')
                    print_error(sock)

def main(args):
    if len(args) < 2:
        print_blue('Client')
        print_blue('  USAGE:', end=" ")
        usage = args[0] + ' <IP:port>'
        print_blue(usage)
        sys.exit(0)

    print_warning(args)

    host, port = args[1].split(":")
    client = Client(host, port)

    client.start()

if __name__ == '__main__':
    main(sys.argv)
