
# coding=utf-8
import socket


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return


def checkVulns(banner):
    if 'vsFTPd' in banner:
        print('[+] vsFTPd is vulnerable.')
    elif 'FreeFloat Ftp Server' in banner:
        print('[+] FreeFloat Ftp Server is vulnerable.')
    else:
        print('[-] FTP Server is not vulnerable.')
    return


def main():
    portList = [21, 22, 25, 80, 110, 443]
    ip = '202.118.65.164'
    for port in portList:
        banner = retBanner(ip, port)
        if banner:
            print('[+] ' + ip + ':' + str(port) + '--' + banner)
            if port == 21:
                checkVulns(banner)


if __name__ == '__main__':
    main()
