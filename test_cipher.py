from Encryption import Cipher
from Encryption import Breaker

my_cipher = Cipher()

mess = input("Give me a message to encrypt: ")
key = int(input("What is the key: "))
enc_mess = my_cipher.encrypt(mess,key)
print(enc_mess)
print("Now I will decrypt your original message without the key")
breaker = Breaker()
possible_solutions = breaker.brute_force(enc_mess, True) 

print(possible_solutions[0])
