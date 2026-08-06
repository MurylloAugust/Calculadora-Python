def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b


while True:
    print("\n--- CALCULADORA ---")

    # 1. Pede o primeiro número
    num1 = float(input("Digite o primeiro número: "))

    # 2. Pede a operação
    operacao = input("Digite a operação (+, -, *, /): ")

    # 3. Pede o segundo número
    num2 = float(input("Digite o segundo número: "))

    # 4. Faz a conta
    if operacao == "+":
        resultado = somar(num1, num2)
    elif operacao == "-":
        resultado = subtrair(num1, num2)
    elif operacao == "*":
        resultado = multiplicar(num1, num2)
    elif operacao == "/":
        resultado = dividir(num1, num2)
    else:
        resultado = "Operação inválida"

    print("Resultado:", resultado)
