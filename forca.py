print('*********************************')
print('***Bem vindo ao jogo da Forca!***')
print('*********************************')

palavra_secreta = "banana"
letras_acertadas = ['_'] * len(palavra_secreta)  # Gera lista ['_', '_', ...] do tamanho certo

acertou = False
enforcou = False
erros = 0

# Imprime as letras descobertas até o momento
print(letras_acertadas)


while (not acertou and not enforcou):
    chute = input("Digite a letra: ")
    acertou_letra = False
    
    posicao = 0
        
    # Percorre cada letra da palavra secreta
    for letra in palavra_secreta:
        
        if chute.upper() == letra.upper():
            letras_acertadas[posicao] = letra.upper()
            acertou_letra = True
        posicao += 1

    # Se não existir, conta um erro
    if not acertou_letra:
        erros += 1
        print(f"Você errou! Restam {6-erros} tentativas")
            
    # Se erros == 6, jogador perde (enforcou = True)
    enforcou = erros == 6
    
    # Se não existir mais '_' na lista, jogador ganha (acertou = True)
    acertou = '_' not in letras_acertadas

    # Mostra o progresso atual    
    print(letras_acertadas)
  
  
if (acertou):
    print("Você acertou!!")
else:
    print ("Você perdeu!!")

print ("Fim do jogo")
        
