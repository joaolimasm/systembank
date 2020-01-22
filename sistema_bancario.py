saldo =100
while True:
    print("1 - sacar")
    print("2 - depositar")
    print("3 - ver saldo")
    print("4 - sair")
    try:
        escolha = int(input("Digite uma opção"))
        if escolha == 1:
            sacar = float(input("Digite um valor para sacar"))
            if sacar > saldo:
                print("Não foi possível sacar. Valor de saque é maior que o saldo")
            elif sacar <= saldo:
                saldo = saldo - sacar
                print("foi retirado {} da sua conta".format(sacar))
        if escolha == 2:
            depositar = float(input("Digite quanto deseja depositar"))
            if depositar<=0:
                print("não foi possível depositar")
            elif depositar>0:
                saldo = saldo + depositar
        if escolha == 3:
            print(saldo)
        if escolha == 4:
            break
    except:
        print("Opção inválida")
