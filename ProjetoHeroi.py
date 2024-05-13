for i in range(0,3):
    nome = input("Digite o nome do seu héroi: ")
    qtdxp = int(input("Digite o xp do seu héroi: "))
    print(nome)

    if(qtdxp <= 1000):
        print("O Héroi de nome " + nome +  " está no nível de Ferro")
    elif(qtdxp <= 2000):
        print("O Héroi de nome " + nome +  " está no nível de Bronze")
    elif(qtdxp <= 5000):
        print("O Héroi de nome " + nome +  " está no nível de Prata")
    elif(qtdxp <= 7000):
        print("O Héroi de nome " + nome +  " está no nível de Ouro")
    elif(qtdxp <= 8000):
        print("O Héroi de nome " + nome +  " está no nível de Platina")
    elif( qtdxp <= 9000):
        print("O Héroi de nome " + nome +  " está no nível de Ascendente")
    elif(qtdxp <= 10000):
        print("O Héroi de nome " + nome +  " está no nível de Imortal")                    
    else:
        print("O Héroi de nome " + nome +  " está no nível de Radiante")







