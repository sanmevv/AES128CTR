import pickle
import socket
import binascii

from pip._vendor.colorama import Fore

import CTR
from CTR.CTR import _encryption
from CTR.CTR import _decryption
message1=[]
m=[]
s2 = socket.socket()
s2.bind(('127.0.0.1',2001))
s2.connect(('127.0.0.1',2000))

def encrypt():
    Input = input(Fore.WHITE +'enter message to bob :')
    message1 = CTR.CTR._encryption((Input))
    print(Fore.RED+"Ciphertext : ",binascii.hexlify(message1[0]))
    m.append(message1[1])
    m.append(message1[2])
    data = pickle.dumps(m)
    s2.send(message1[0])
    s2.send(data)
def decrypt():
    m.clear()
    message1.clear()
    response1 = s2.recv(1024)
    response2 = s2.recv(1024)
    resp2 = pickle.loads(response2)
    message = CTR.CTR._decryption(response1, resp2[0], resp2[1])
    print(Fore.BLUE+'Message from Bob : ', str(message, 'utf-8'))
def loop():
    while True:
        decrypt()
        encrypt()
print(Fore.YELLOW+ "Hello Alice, this application is using AES-128 bit CTR Mode Algorithm for Encryption and Decryption\n"
      "The AES-128 bit CTR Mode Algorithm gracefully encrypts and decrypts data, weaving an intricate tapestry of protection and confidentiality by utilizing Socket Programming!")
loop()

