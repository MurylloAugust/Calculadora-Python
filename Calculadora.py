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


def porcentagem(a, b):
    return (a * b) / 100


def raiz_quadrada(a):
    if a < 0:
        return "Não é possível calcular a raiz quadrada de um número negativo!"
    return a**0.5


while True:
    print("\n--- CALCULADORA ---")

    # 1. Pede o primeiro número
    num1 = float(input("Digite o primeiro número: "))

    # 2. Pede a operação
    operacao = input("Digite a operação (+, -, *, /, %, sqrt): ")

    if operacao == "sqrt":
        # Para raiz quadrada e porcentagem, não precisamos do segundo número
        num2 = None
    else:
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
    elif operacao == "%":
        resultado = porcentagem(num1, num2)
    elif operacao == "sqrt":
        resultado = raiz_quadrada(num1)
    else:
        resultado = "Operação inválida"

    print("Resultado:", resultado)
