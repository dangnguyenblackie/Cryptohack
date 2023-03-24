#!/usr/bin/env python3

import sys
import base64
from Crypto.Util.number import *
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")
############### INTRO
#2
# ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# print("Here is your flag:")
# print("".join(chr(o) for o in ords))


#3
# cipher = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# print(bytes.fromhex(cipher))

#4
cipher = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

print(base64.b64encode(bytes.fromhex(cipher)))
