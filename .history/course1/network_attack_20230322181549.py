#!/usr/bin/env python3

import telnetlib
import json

HOST = "socket.cryptohack.org"
PORT = 11112

tn = telnetlib.Telnet(HOST, PORT)


def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

for i in range(5):
    print(readline())
    print(readline())
    print(readline())
    print(readline())


    request = {
        'error': 'Sorry! All we have to sell are flags.'
    }
    json_send(request)

    response = json_recv()

    print(response)
