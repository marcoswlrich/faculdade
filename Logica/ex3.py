# Cabeçalho do jogo
print("       HOTEL DOS ANIMAIS")
print("Especificando posição: ")
print("[1, 2, 3, 4]")
print("[5, 6, 7, 8]")
print()
print("-----Bem vindo a fase 1!-----")
print()
print("Na Fase 1, você deve alocar o Rato e o Gato na seguinte matriz que representa os quartos: ")
print("['*', '*', '_', 'G']")
print("['R', '_', '*', '*']")

# Variáveis de números inteiros digitados pelo usuário
rato = int(input("Em qual posição você quer alocar o Rato? "))
gato = int(input("Em qual posição você quer alocar o Gato? "))
print()

# Estruturas de condições para analisar a resposta do usuário
# se a condição if for verdadeira a estrutura continua e imprime os resultados na tela
# se for falsa se encerra com o else.

# Primeira estrutura de condição que analisa respostas do usuário na primeira fase
if (rato == 6 and gato == 3):

    # Resposta se a condição for verdadeira para ir para a segunda fase.
    print("Parabéns você acertou! Vamos para a segunda fase!")
    print()
    print("-----Bem vindo a fase 2-----")
    print()
    print("Na fase 2, você deve alocar: CÃO, CÃO e OSSO")
    print("['_', '*', '*', '*']")
    print("['*', 'C', '_', '_']")

    # Variáveis de números inteiros da segunda fase
    cao1 = int(input("Em qual posição você quer alocar o primeiro Cão? "))
    cao2 = int(input("Em qual posição você quer alocar o segundo Cão? "))
    osso = int(input("Em qual posição você quer alocar o Osso? "))
    print()
    # Segunda estrutura de condição que analisa respostas do usuário na segunda fase
    if((osso == 1 and cao1 == 7 and cao2 == 8) or (osso == 1 and cao1 == 8 and cao2 == 7)):

        # Resposta se a condição for verdadeira para ir para a terceira fase.
        print("Parabéns você acertou! Vamos para a terceira fase!")
        print()
        print("-----Bem vindo a fase 3-----")
        print()
        print("Na fase 3, você deve alocar: GATO, RATO e OSSO")
        print("['_', '*', '*', '*']")
        print("['_', 'G', '_', '*']")

        # Variáveis de números inteiros da terceira fase
        gato = int(input("Em qual posição você quer alocar o Gato? "))
        osso = int(input("Em qual posição você quer alocar o Osso? "))
        rato = int(input("Em qual posição você quer alocar o Rato? "))
        print()

        # Terceira estrutura de condição que analisa respostas do usuário na terceira fase
        if(rato == 1 and osso == 5 and gato == 7):

            # Resposta se a condição for verdadeira para ir para a quarta fase.
            print("Parabéns você acertou! Vamos para a última fase!")
            print()
            print("-----Bem vindo a fase 4-----")
            print()
            print("Na fase 4, você deve alocar: QUEIJO, QUEIJO, OSSO. ")
            print("['_', '_', '_', '*']")
            print("['*', 'R', '*', '*']")

            # Variáveis de números inteiros da quarta fase
            queijo1 = int(input("Em qual posição você quer alocar o primeiro Queijo? "))
            queijo2 = int(input("Em qual posição você quer alocar o segundo Queijo?  "))
            osso = int(input("Em qual posição você quer alocar o Osso? "))

            # Quarta estrutura de condição que analisa respostas do usuário na quarta fase
            if((osso == 2 and queijo1 == 3 and queijo2 == 1) or (osso == 2 and queijo1 == 1 and queijo2 == 3)):

                # Resposta se a condição for verdadeira para vencer o jogo
                print("Você ganhou!")


            # else da quarta estrutura de condição
            else:
                print("Você perdeu!")
         #else da terceira estrutura de condição
        else:
            print("Você perdeu!")
     #else da segunda estrutura de condição
    else:
        print("Você perdeu!")
# else da primeira estrutura de condição
else:
    print("Você perdeu!")
