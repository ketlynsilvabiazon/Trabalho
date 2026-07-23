import random

naipes_simbolos = ['♣', '♦', '♥', '♠']
nomes = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
valores = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def criar_baralho():
    baralho = []

    for naipe in naipes_simbolos:
        for i in range(len(nomes)):
            baralho.append([nomes[i] + naipe, valores[i]])

    random.shuffle(baralho)
    return baralho

def calcular_total(mao):                      # Função que soma os pontos das cartas

    total = 0
    ases = 0

    for carta in mao:                         # Soma todas as cartas do baralho
        total += carta[1]

        if carta[0][:-1] == 'A':              # Conta quantos "ases" existem
            ases += 1

    while total > 21 and ases > 0:            # Se passar de 21, o Ás passa a valer 1

        total -= 10
        ases -= 1

    return total

baralho = criar_baralho()
saldo = 500

print("\n========== Bem-vindo ao Blackjack! ==========")

while True:
    try:
        iniciar = int(input("\nDeseja jogar?\n1 - Sim\n0 - Não\nEscolha: "))

        if iniciar == 1:
            break

        elif iniciar == 0:
            print("\nObrigado por jogar!")
            break

        else:
            print("\nDigite apenas 1 ou 0.")

    except ValueError:
        print("\nDigite um número válido.")

if iniciar == 0:
    print("Jogo encerrado.")
else:
    while True:
        if saldo <= 0:
            print("\nVocê ficou sem saldo.")
            print("Game Over!!!")

            while True:
                try:

                    reiniciar = int(input(
                        "\nDeseja começar novamente?\n"
                        "1 - Sim\n"
                        "0 - Não\n"
                        "Escolha: "
                    ))

                    if reiniciar == 1:
                        saldo = 500
                        baralho = criar_baralho()
                        print("\nNovo jogo iniciado!")
                        break

                    elif reiniciar == 0:
                        print("\nObrigado por jogar!")
                        break

                    else:
                        print("\nDigite apenas 1 ou 0.")

                except ValueError:
                    print("\nDigite um número.")

            if reiniciar == 0:
                break

        print("\n======================")
        print("Saldo atual: R$", saldo)
        print("======================")

        while True:
            try:
                aposta = int(input("\nDigite o valor da aposta: "))

                if aposta <= 0:
                    print("\nAposta inválida.")
                    print("A aposta deve ser maior que zero.")

                elif aposta > saldo:
                    print("\nSaldo insuficiente.")

                else:
                    break

            except ValueError:
                print("\nDigite um número.")

        if len(baralho) < 10:                                                             # cria um baralho "novo" se não tiver cartas o suficiente no jogo
            baralho = criar_baralho()

        jogador = []
        mesa = []

        jogador.append(baralho.pop())
        jogador.append(baralho.pop())

        mesa.append(baralho.pop())
        mesa.append(baralho.pop())

        while True:
            total_jogador = calcular_total(jogador)
            cartas_jogador = []

            for carta in jogador:

                cartas_jogador.append(carta[0])

            print("\nCartas do jogador:", cartas_jogador)
            print("Total do jogador:", total_jogador)
            print("Carta visível da mesa:", mesa[0][0])

            if total_jogador > 21:
                print("\nVocê estourou! Passou de 21.")
                break

            elif total_jogador == 21:
                print("\nVocê fez 21 pontos!")
                break

            while True:

                try:

                    resposta = int(input(
                        "\nDeseja mais cartas?\n"
                        "1 - Sim\n"
                        "0 - Não\n"
                        "Escolha: "
                    ))

                    if resposta == 1:

                        nova_carta = baralho.pop()
                        jogador.append(nova_carta)

                        print("\nVocê comprou:", nova_carta[0])
                        break

                    elif resposta == 0:
                        break

                    else:
                        print("\nDigite apenas 1 ou 0.")

                except ValueError:
                    print("\nDigite um número.")

            if resposta == 0:
                break

        total_jogador = calcular_total(jogador)

        if total_jogador <= 21:

            print("\n--- Turno da mesa ---")

            while calcular_total(mesa) < 17:
                nova_carta = baralho.pop()
                mesa.append(nova_carta)
                print("Mesa comprou:", nova_carta[0])

            cartas_mesa = []

            for carta in mesa:
                cartas_mesa.append(carta[0])

            total_mesa = calcular_total(mesa)

            print("\nCartas da mesa:", cartas_mesa)
            print("Total da mesa:", total_mesa)

            if total_mesa > 21:
                print("\nMesa estourou. Você ganhou!")
                saldo += aposta

            elif total_jogador > total_mesa:
                print("\nVocê ganhou!")
                saldo += aposta

            elif total_jogador < total_mesa:
                print("\nVocê perdeu!")
                saldo -= aposta

            else:
                print("\nEmpate!")
                saldo += aposta

        else:
            print("\nVocê perdeu!")
            saldo -= aposta

        print("\nSaldo atual: R$", saldo)

        continuar = input("\nDeseja continuar jogando? (S/N): ").upper()

        if continuar == "S":
            continue

        elif continuar == "N":
            print("\nObrigado por jogar!")
            break

        else:
            print("\nOpção inválida. Encerrando.")
            break





    # import random
# naipes_simbolos = ['♣', '♦', '♥', '♠']
# nomes = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# valores = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
# baralho = []

# for naipe in naipes_simbolos:
#     for i in range(len(nomes)):
#         baralho.append([nomes[i] + naipe, valores[i]])
# random.shuffle(baralho)
# saldo = 500

# def calcular_total(mao):                      # Função que soma os pontos das cartas
#     total = 0
#     ases = 0
#     for carta in mao:                         # Soma todas as cartas do baralho 
#         total += carta[1]
#         if carta[0][0] == 'A':                # Conta quantos "ases" existem
#             ases += 1
#     while total > 21 and ases > 0:            # Se passar de 21, o Ás passa a valer 1
#         total -= 10
#         ases -= 1
#     return total

# print("\n========== Bem-vindo ao Blackjack! ==========")

# while True:

#     try:
#         iniciar = int(input("\nDeseja jogar?\n1 - Sim\n0 - Não\n\nEscolha: "))
#         if iniciar == 1:
#             break
#         elif iniciar == 0:
#             print("\nObrigado por jogar!")
#             break
#         else:
#             print("\nDigite apenas 1 ou 0.")

#     except ValueError:
#         print("\nVocê não digitou um numero.")
#         print("Por favor, digite um número válido.")

# while iniciar == 1 and saldo > 0:
#     print("\nSeu saldo é de R$", saldo)

#     try:
#         aposta = int(input("Digite o valor da aposta: "))
#     except ValueError:
#         print("\nVocê não digitou um número.")
#         print("Digite um número válido.")
#         continue

#     if aposta > saldo or aposta <= 0:
#         print("\nAposta inválida ou saldo insuficiente.")
#         continue

#     if len(baralho) < 10:                                                  #cria um baralho "novo" se não tiver cartas o suficiente no jogo
#         baralho = []
#         for naipe in naipes_simbolos:
#             for i in range(len(nomes)):
#                 baralho.append([nomes[i] + naipe, valores[i]])
#         random.shuffle(baralho)

#     jogador = []
#     mesa = []

#     jogador.append(baralho.pop())
#     jogador.append(baralho.pop())

#     mesa.append(baralho.pop())
#     mesa.append(baralho.pop())

#     while True:
#         total_jogador = calcular_total(jogador)
#         cartas_jogador = []

#         for carta in jogador:
#             cartas_jogador.append(carta[0])

#         print("\nCartas do jogador:", cartas_jogador)
#         print("Total do jogador:", total_jogador)
#         print("Carta visível da mesa:", mesa[0][0])

#         if total_jogador > 21:
#             print("\nVocê estourou! Passou de 21.")
#             break

#         elif total_jogador == 21:
#             print("\nVocê fez 21 pontos!")
#             break

#         try:
#             resposta = int(input("\nDeseja mais cartas? (1-Sim / 0-Não): "))

#         except ValueError:
#             print("\nVocê não digitou um número.")
#             print("Digite um número válido.")
#             resposta = 0

#         if resposta == 1:
#             nova_carta = baralho.pop()
#             jogador.append(nova_carta)
#             print("Você comprou:", nova_carta[0])
#             print("Total atual:", calcular_total(jogador))

#         else:
#             break

#     total_jogador = calcular_total(jogador)

#     if total_jogador <= 21:

#         print("\n--- Turno da mesa ---")
#         cartas_mesa = []

#         for carta in mesa:
#             cartas_mesa.append(carta[0])

#         print("Cartas da mesa:", cartas_mesa)
#         print("Total da mesa:", calcular_total(mesa))

#         while calcular_total(mesa) < 17:

#             nova_carta = baralho.pop()
#             mesa.append(nova_carta)
#             print("Mesa comprou:", nova_carta[0])
#             print("Novo total da mesa:", calcular_total(mesa))
#         total_mesa = calcular_total(mesa)
#         cartas_mesa = []

#         for carta in mesa:
#             cartas_mesa.append(carta[0])

#         print("\nResultado final da mesa:")
#         print("Cartas:", cartas_mesa)
#         print("Total:", total_mesa)

#         if total_mesa > 21:

#             print("\nA mesa estourou! Você ganhou!")
#             saldo += aposta

#         elif total_jogador > total_mesa:
#             print("\nVocê fez mais pontos! Você ganhou!")
#             saldo += aposta

#         elif total_jogador < total_mesa:
#             print("\nA mesa fez mais pontos. Você perdeu!")
#             saldo -= aposta

#         else:
#             print("\nEmpate!")

#     else:
#         print("\nVocê perdeu!")
#         saldo -= aposta
#     print("\nSaldo atual: R$", saldo)

# if saldo <= 0:
#     print("\nVocê ficou sem saldo.")
#     print("Game Over!!!")

#     while True:
#         try:
#             reiniciar = int(input("\nDeseja começar novamente?\n1 - Sim\n0 - Não\nEscolha: "))

#             if reiniciar == 1:
#                 saldo = 500
#                 print("\nNovo jogo iniciado!")
#                 break
#             elif reiniciar == 0:
#                 print("\nObrigado por jogar!")
#                 exit()
#             else:
#                 print("\nDigite apenas 1 ou 0.")
#         except ValueError:
#             print("\nDigite um número.")

#     continuar = "S"