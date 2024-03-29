import socket
ip = '127.0.0.1'


def get_pvt_ip():
    try:
        # add try catch block later
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('10.255.255.255', 1))

        # Get the local IP address assigned by the operating system
        # This is the Link-local Ipv6 Address
        private_ip = s.getsockname()[0]

        # Close the socket
        s.close()

        return private_ip
    except Exception as e:
        print(f"Error : {e}")
        return 0

def test_pvt_ip():
    IP = get_pvt_ip()
    print("Running Test IP\n")

    if IP == '192.168.244.199':
        return 1
    else :
        return 0

test_pvt_ip()

