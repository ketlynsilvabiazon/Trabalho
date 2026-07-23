newFile = []
qty = 0
with open("./clientes.txt", 'r', encoding="iso-8859-1") as file:
    for line in file.readlines():
        newLine = []
        for char in line:
            if (char.isalpha() or char.isspace()):
                newLine.append(char)
        newLineStr = ''.join(newLine)
        newLineStr = newLineStr.split(' ')

        for i in range(len(newLineStr)):
            newLineStr[i] = newLineStr[i].capitalize()
        
        newLineStr = ' '.join(newLineStr)
        newFile.append(newLineStr)
        qty += 1



with open("./clientes_recuperado.txt", 'w', encoding="iso-8859-1") as file:
    file.write(''.join(newFile))

print(qty)