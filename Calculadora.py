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


def exponencial(a, b):
    if b == 0:
        return "1"
    return a**b


def raiz_cubica(a):
    if a < 0:
        return -((-a) ** (1 / 3))
    return a ** (1 / 3)


def obter_numero(mensagem):
    """Lida com a leitura de números, tratamento de erro e comando de saída."""
    while True:
        entrada = input(mensagem).strip().lower()
        if entrada == "sair":
            return "sair"
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida! Digite um número válido ou 'sair'.")


while True:
    print("\n--- CALCULADORA ---")
    print("Digite 'sair' para encerrar o programa.")

    # 1. Pede o primeiro número
    num1 = obter_numero("Digite o primeiro número: ")
    if num1 == "sair":
        print("Encerrando o programa...")
        break

    # 2. Pede a operação
    operacao = input("Digite a operação (+, -, *, /, %, sqrt, **, cbrt): ")
    if operacao == "sair":
        print("Encerrando o programa...")
        break

    if operacao == "sqrt":
        # Para raiz quadrada e porcentagem, não precisamos do segundo número
        num2 = None
    elif operacao == "cbrt":
        # Para raiz cúbica, não precisamos do segundo número
        num2 = None
    else:
        # 3. Pede o segundo número
        num2 = obter_numero("Digite o segundo número: ")
        if num2 == "sair":
            print("Encerrando o programa...")
            break

    # 4. Faz a conta
    if operacao == "+":
        resultado = somar(num1, num2)
    elif operacao == "**":
        resultado = exponencial(num1, num2)
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
    elif operacao == "cbrt":
        resultado = raiz_cubica(num1)
    else:
        resultado = "Operação inválida"

    print("Resultado:", resultado)
