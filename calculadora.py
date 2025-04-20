#definindo funções e variáveis

def somar (x, y):
    return x + y

def subtrair (x, y):
    return x - y

def multiplicar (x, y):
    return x * y

def dividir (x, y):
    if y == 0:
        return "Nunca dividirás por ZERO!!"
    return x / y

print ('Seja bem-vindo à calculadora!')

opr = input("Escolha a operação (+, -, *, /): ")
n1 = float(input("Digite o primeiro número da operação: "))
n2 = float(input("Digite o segundo número da operação: "))

#chamando as funções e variáveis

if opr == '+':
    resp = somar(n1, n2)

elif opr == '-':
    resp = subtrair(n1, n2)

elif opr == '*':
    resp = multiplicar(n1, n2)

elif opr == '/':
    resp = dividir(n1, n2)

else: 
    resp = "Operação inválida! Tente novamente"

print("A resposta é:", resp)