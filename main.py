import Key_Generation
import Dna_Encryption
import Dna_Decryption
import random
import math
import key_pair_generation

print("\n\n\t\t<--------SENDER SIDE------->\n\n")

from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.connect(("localhost",80))

print("\n\n<--------receiving email address from receiver.....------->")
print("<--------receiving mac id from receiver.....------->")
print("<--------receiving pan number from receiver.....------->\n\n")

cipher1=s.recv(5000)
cipher2=s.recv(5000)
cipher3=s.recv(5000)

email1=cipher1.decode()
mac1=cipher2.decode()
pan1=cipher3.decode()

email=key_pair_generation.decryption(email1)
mac=key_pair_generation.decryption(mac1)
pan=key_pair_generation.decryption(pan1)

key=Key_Generation.Key_Generation(email,mac,pan)
Cipher_Text=Dna_Encryption.Dna_Encryption(key)
s.send(bytes(   Cipher_Text  ,'utf8'))
#Dna_Decryption.Dna_Decryption(Cipher_Text,key)
s.close()
