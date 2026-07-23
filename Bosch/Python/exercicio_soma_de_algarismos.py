num2 = 0


while True:
    try:
        num = int(input("Insira um número maior que zero: "))
        
        
        if num <= 0 :
            raise Exception
        for i in str(num):
            num2 = int(i) + num2
            break
            
    except:
        print("data inválida. Digite novamente")
    print(f'a soma dos algarismos {num2}')