# # Crie um programa e que o usuario escolhe uma palavra e o 
# # programa diz quantas vezes essa palavra aparece no arquivo.

# # Dica: Utilize as funçoes split e strip.

# arquivo = open('texto.txt', 'r', encoding='utf-8')
# palavra = input('Digite a palavra que deseja procurar: ')
# contador = 0
# for linha in arquivo:
#     palavras = linha.strip().lower().split()
#     for item in palavras:
#         if item == palavra:
#             contador += 1
# arquivo.close()
# print(f"A palavra '{palavra}' aparece {contador} vez(es) no arquivo."


