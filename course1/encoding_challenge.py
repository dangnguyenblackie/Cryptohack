# # #!/usr/bin/env python3

# # from Crypto.Util.number import bytes_to_long, long_to_bytes
# # # from utils import listener # this is cryptohack's server-side module and not part of python
# # import base64
# # import codecs
# # import random

# # FLAG = "crypto{????????????????????}"
# # ENCODINGS = [
# #     "base64",
# #     "hex",
# #     "rot13",
# #     "bigint",
# #     "utf-8",
# # ]
# # with open('/usr/share/dict/words') as f:
# #     WORDS = [line.strip().replace("'", "") for line in f.readlines()]


# # class Challenge():
# #     def __init__(self):
# #         self.challenge_words = ""
# #         self.stage = 0

# #     def create_level(self):
# #         self.stage += 1
# #         self.challenge_words = "_".join(random.choices(WORDS, k=3))
# #         encoding = random.choice(ENCODINGS)

# #         if encoding == "base64":
# #             encoded = base64.b64encode(self.challenge_words.encode()).decode() # wow so encode
# #         elif encoding == "hex":
# #             encoded = self.challenge_words.encode().hex()
# #         elif encoding == "rot13":
# #             encoded = codecs.encode(self.challenge_words, 'rot_13')
# #         elif encoding == "bigint":
# #             encoded = hex(bytes_to_long(self.challenge_words.encode()))
# #         elif encoding == "utf-8":
# #             encoded = [ord(b) for b in self.challenge_words]

# #         return {"type": encoding, "encoded": encoded}

# #     #
# #     # This challenge function is called on your input, which must be JSON
# #     # encoded
# #     #
# #     def challenge(self, your_input):
# #         if self.stage == 0:
# #             return self.create_level()
# #         elif self.stage == 100:
# #             self.exit = True
# #             return {"flag": FLAG}

# #         if self.challenge_words == your_input["decoded"]:
# #             return self.create_level()

# #         return {"error": "Decoding fail"}


# # listener.start_server(port=13377)


from pwn import * # pip install pwntools
import json
import sys
import base64
from Crypto.Util.number import long_to_bytes
from pwn import *
from binascii import unhexlify
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


received = json_recv()

def decoded(encoded, type_encode):
    decode_str = ""
    if type_encode == "base64":
        decode_str = str(base64.b64decode(encoded))[2:-1]
    elif type_encode == "hex":
        decode_str = str(bytes.fromhex(encoded))[2:-1]
    elif type_encode == "rot13":
        decode_str = codecs.decode(encoded, 'rot_13')
    elif type_encode == "bigint":
        decode_str = str(long_to_bytes(int(encoded,16)))[2:-1]
    elif type_encode == "utf-8":
        decode_str = "".join(chr(item) for item in encoded)
    print(decode_str)
    return (decode_str)

for i in range(100):
    
    
    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])
    to_send = {
        "decoded": (decoded(received["encoded"],received["type"]))
    }
    print("Send:\n\n")
    print(to_send)
    json_send(to_send)
    received = json_recv()
