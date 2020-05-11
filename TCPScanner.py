from socket import *

i = 0
ports = [1, 2, 3, 4, 5, 6]


def portScan(host, port):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, int(port)))
        print(f"Host: {host} tcp/{str(port)} open")
    except:
        print(f"Host: {host} tcp/{str(port)} closed")

def main():
    host = str(input("Host: "))
    portNum = int(input("Number of ports (MAX = 6 PORTS): "))
    for i in range(0, portNum):       
        ports[i] = int(input())
        i += 1

    setdefaulttimeout(1)
    host_ip = gethostbyname(host)

    for port in ports:
        portScan(host, port)

main()
