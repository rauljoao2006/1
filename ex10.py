import random

numero = random.randint(1, 100)
tentativas = 0

print("adivinha o número entre 1 e 100")

while True:
    palpite = int(input("digita um número: "))
    tentativas += 1

    if palpite < numero:
        print("muito baixo")
    elif palpite > numero:
        print("muito alto")
    else:
        print("acertou!")
        print("numero de tentativas:", tentativas)
        break