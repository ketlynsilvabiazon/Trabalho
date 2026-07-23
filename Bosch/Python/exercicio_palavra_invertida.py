palavra = input('Digite a palavra: ')

nova_palavra = palavra.replace(" ","")
nova_palavra = nova_palavra.lower()

# invertida = nova_palavra [::-1]    #PRIMEIRA FORMA

lista = list(nova_palavra)           #SEGUNDA FORMA
lista.reverse()
invertida = "".join(lista)

print('A palavra:',palavra)
print('Ao contrario:',invertida)

if nova_palavra == invertida:
    print(f'{palavra} é um palindromo')
else:
    print(f'{palavra} não é um palindromo')
    