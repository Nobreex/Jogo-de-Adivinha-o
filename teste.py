import random

# Gera um número secreto entre 1 e 10
numero_secreto = random.randint(1, 5)

print("Olá! Vamos jogar um jogo! 🎮")
print("Tente adivinhar o número entre 1 e 5.")

# Pede para o jogador digitar um número
tentativa = int(input("Qual número você acha que é? "))

# Verifica se o jogador acertou
if tentativa == numero_secreto:
    print("Parabéns! 🎉 Você acertou!")
else:
    print(f"Ah, não! 😢 O número era {numero_secreto}. Tente novamente!")

