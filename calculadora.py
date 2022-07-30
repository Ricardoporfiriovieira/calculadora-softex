def calculador(num1, num2, op):
    if(op == 1):
        return num1 + num2
    elif(op == 2):
        return num1 - num2
    elif(op == 3):
        return num1 * num2
    elif(op == 4):
        return num1 / num2
    else: 
        return 0


numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
print(" 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão ")
operacao = int(input("Digite a operação desejada: "))


print(f"Resultado: {calculador(numero1, numero2, operacao)}")