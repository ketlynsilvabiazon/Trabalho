# Atividade
# exibir quantidade de caracteres
# contar quantas vezes cada palavra se repete
# quantidade de linhas que o poema tem 
# contar quantas palavras tem no total

palavras_poema = []                         
quantidade = []

quantidade_linhas = 0                       
quantidade_palavras = 0
quantidade_caracteres = 0

with open("poema.txt", 'r', encoding='utf-8')as arquivo:  # para funciona tem que retirar da pasta exercicio de arquivo
    for linha in arquivo.readlines():
       
        quantidade_linhas = quantidade_linhas + 1 
        quantidade_caracteres += len(linha)
        palavras = linha.split()
        quantidade_palavras += len(palavras)

        for palavra in palavras:
            palavra = palavra.lower()

            palavra = palavra.replace(",", "")
            palavra = palavra.replace(".", "")
            palavra = palavra.replace("!", "")
            palavra = palavra.replace("?", "")
            palavra = palavra.replace(";", "")
            palavra = palavra.replace(":", "")

            if palavra != "":
                achou = False
                
                for i in range(len(palavras_poema)):
                    if palavras_poema[i] == palavra:
                        quantidade[i] += 1
                        achou = True
                        break
                if achou == False:
                    palavras_poema.append(palavra)
                    quantidade.append(1)

print("Quantidade de caracteres:", quantidade_caracteres)
print("Quantidade de linhas:", quantidade_linhas)
print("Quantidade total de palavras:", quantidade_palavras)
print("\nQuantidade de vezes que cada palavra aparece") 

for i in range(len(palavras_poema)):
    print(palavras_poema[i], ":", quantidade[i])