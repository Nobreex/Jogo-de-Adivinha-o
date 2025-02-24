import random


numero_secreto = random.randint(1, 5)

print("Olá! Vamos jogar um jogo?")
print("Tente adivinhar o número entre 1 e 5.")


tentativa = int(input("Qual número você acha que é? "))


if tentativa == numero_secreto:
    print("Parabéns! Você acertou!")
else:
    print("Ah, não! O número era {numero_secreto}. Tente novamente!")

