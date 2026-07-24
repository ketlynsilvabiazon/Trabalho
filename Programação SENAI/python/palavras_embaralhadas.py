import random

arquivo = open('palavras.txt' , 'r', encoding='utf-8')

pontos = 100
desconto_por_erro = int(input('Quantos pontos deseja perder se você errar(20 a 100)?: '))
nível = input('Qual a dificuldade de palavra que você deseja(1, 2, ou 3)?: ')

#filtra as palavras
linhas = arquivo.readlines()
arquivo.close()

#marcador de dificuldade
if nível == '1':
    marcador = '[FACEIS]' 
elif nível == '2':
    marcador = '[MEDIAS]'
else:
    marcador = '[DIFICEIS]'

#Filtrar lista
palavras_do_nível = []
achou_secao = False

for linha in linhas:
    linha = linha.strip()
    if linha.strip() == marcador:
        achou_secao = True
        continue
    if achou_secao: 
        palavras_do_nível.append(linha)

palavra_original = random.choice(palavras_do_nível)
lista_letras = list(palavra_original)
random.shuffle(lista_letras)
palavra_embaralhada = "".join(lista_letras)

print(f'Palavra escolhida: {palavra_embaralhada}.')
tentativa = input("R: ")
if tentativa.lower() == palavra_original.lower():
    print('Parabéns!!! Você acertou a palavra.')
else:
    pontos -= desconto_por_erro
    print(f'Sinto muito, você acaba de perder {desconto_por_erro} pontos.')
    if pontos <= 0:
        print(f'Você perdeu! A palavra era: {palavra_original}.')
    else:
        print(f'Pontos restantes: {pontos}.')













for linha in linhas:
    linha_limpa = linha.strip()
    if linha_limpa in ['[FACEIS]','[MEDIAS]','[DIFICEIS]']:
        if linha_limpa == marcador:
            achou_secao = True
        else:
            achou_secao = False
        continue
    if achou_secao: 
        palavras_do_nível.append(linha)
    if achou_secao and linha_limpa != '':