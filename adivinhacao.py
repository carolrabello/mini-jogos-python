import random

print('*********************************')
print('Bem vindo(a) ao jogo da Adivinhação!')
print('*********************************')

numero_secreto = random.randint(1, 100)

print("\nEscolha seu nível de dificuldade: ")
print("1 - 15 tentativas\n2 - 10 tentativas\n3 - 5 tentativas")
opcao = int(input())

niveis = {1: 20, 2: 10, 3: 5}


for rodada in range (1, niveis[opcao] + 1):
    chute = int(input("Digite um numero entre 1 e 100: "))

    if chute == numero_secreto:
        print("Você acertou!!")
        break
    elif chute < numero_secreto:
        print(f"Você errou! O numero secreto é maior do que {chute}")
    else:
        print(f"Você errou! O numero secreto é menor do que {chute}")
        
    if (niveis[opcao] - rodada) == 0:
        print("Você perdeu!")
        break

    print(f"Você tem mais {niveis[opcao] - rodada} tentativas\n")

print(f"\nO numero secreto era {numero_secreto}!")
print("\nFim de jogo!")