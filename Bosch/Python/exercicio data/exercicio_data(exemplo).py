while True:
    try:
        data = input("Digite uma data ")
        data = data.split("/")

        if len(data)!=3:
            raise Exception
        elif int(data[0])<1 or int(data[0])>31:
            raise Exception
        elif int(data[1])<1 or (int(data[1]))>12:
            raise Exception
        elif len(data[0])!=2 or len(data[1])!=2 or len(data[2])!=4:
            raise Exception
        
        meses = ['janeiro','fevereiro','março','abril','maio']

        print(f'Data por extenso: {data[0]} de {meses[int(data[1])-1]} de {data[2]}')
        break
    except:
        print("Data inválida. Digite novamente")