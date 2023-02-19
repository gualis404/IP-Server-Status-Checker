import requests
import threading
import random
import struct
import socket

threads = input('İstek sayısı: ')

def get(ip):
    endpoint = f'https://ipinfo.io/{ip}/json'
    response = requests.get(endpoint, verify = True)

    try:
        return response.json()['country']
    except:
        return 'Unknown'

validStatusCodes = [200, 301, 302, 401, 403, 404, 500, 503]

def request(ip, port):
    try:
        r = requests.get('http://{}:{}/'.format(ip, port))
        if not ip.startswith('127'):
            if r.status_code in validStatusCodes:
                print(ip, port, r.headers['Server'], get(ip))
    except:
        pass

for i in range(int(threads)):
    s = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    t = threading.Thread(target=request, args=(s, 80))
    t.start()
