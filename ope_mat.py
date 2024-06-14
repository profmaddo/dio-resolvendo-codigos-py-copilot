# vamos receber dois numeros diferentes do usuário 
# e selecionar uma operação matemática que pode
# ser Adição, Multiplicação, Subtração ou Divisão
# depois apresentar o resultado da operação

# Solicita a entrada do primeiro numero
primeiroNumero = int(input("Digite o primeiro numero: "))

# Solicita a entrada do segundo dado
segundoNumero = int(input("Digite o segundo Numero: "))

operacao = input("Escolha a operação (+, -, * ou /): ")

if operacao == "+":
    print(primeiroNumero + segundoNumero)
elif operacao == "-":
     print(primeiroNumero - segundoNumero)
elif operacao == "*":
     print(primeiroNumero * segundoNumero)  
elif operacao == "/":
     print(primeiroNumero / segundoNumero)  
else:
     print("Operação inválida!")