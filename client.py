import random
import math
import Dna_Decryption
from socket import *
import Key_Generation
import key_pair_generation

print("\n\n\t\t<--------RECEIVER SIDE------->\n\n")
s = socket(AF_INET, SOCK_STREAM)
s.bind(("", 80))
s.listen(5)
c, a = s.accept()

email=input("enter the email")
mac=input("enter the mac")
pan=input("enter the pan")

cipher1=key_pair_generation.encryption(email)
cipher2=key_pair_generation.encryption(mac)
cipher3=key_pair_generation.encryption(pan)

print("\n\n<--------sending email address to sender.....------->")
print("<--------sending mac id to sender.....------->")
print("<--------sending pan number to sender.....------->\n\n")


c.send(bytes(cipher1, 'utf8'))
c.send(bytes(cipher2, 'utf8'))
c.send(bytes(cipher3, 'utf8'))

data = c.recv(5000)
Cipher_Text = data.decode()
if Cipher_Text != "":
    print("\n\n\t\t<--------CIPHER TEXT RECEIVED.....------->\n\n")

key = Key_Generation.Key_Generation(email, mac, pan)
c.close()
Dna_Decryption.Dna_Decryption(Cipher_Text, key)
