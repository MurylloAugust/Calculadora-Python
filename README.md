# Calculadora Científica Python CLI 🧮

Uma calculadora de linha de comando (CLI) desenvolvida em Python, com foco em boas práticas de programação, tratamento de exceções, modularização e expansão para funções científicas avançadas.

## 🚀 Funcionalidades Atuais

### Operações Básicas
- Soma (`+`)
- Subtração (`-`)
- Multiplicação (`*`)
- Divisão (`/`) com validação contra divisão por zero
- Porcentagem (`%`)

### Potenciação e Raízes
- Exponenciação (`**`)
- Raiz Quadrada (`sqrt`) com validação para números negativos
- Raiz Cúbica (`cbrt`) com suporte a números negativos

### Usabilidade e Tratamento de Erros
- Comando de saída (`sair`) funcional em qualquer etapa sem interromper o programa abruptamente
- Tratamento de entradas com `.strip().lower()` para evitar erros com espaços extras ou letras maiúsculas
- Validação de dados via `try/except` (`ValueError`) contra digitações inválidas
- Uso de `raise` para exceções apropriadas

## 📌 Próximas Funcionalidades (Roadmap)

Planejadas para as próximas versões da calculadora:

- **Trigonometria:** Seno (`sin`), Cosseno (`cos`), Tangente (`tan`)
- **Trigonometria Inversa / Hiperbólica:** ArcSen, ArcCos, ArcTan, Sinh, Cosh, Tanh
- **Logaritmos:** Logaritmo natural (`ln`), Logaritmo na base 10 (`log10`), Logaritmo em base arbitrária
- **Constantes Matemáticas:** Integração de π (Pi) e e (Número de Euler)
- **Fatorial e Combinatória:** Fatorial (`n!`), Permutações e Combinações
- **Conversão de Ângulos:** Suporte a Graus e Radianos
- **Histórico de Operações:** Manter registro das últimas operações realizadas

## 🛠️ Pré-requisitos

- Python 3.x instalado
- Nenhuma dependência externa (utiliza apenas a biblioteca padrão do Python)

## 🔧 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/MurylloAugust/Calculadora-Python.git
cd Calculadora-Python
```

2. Execute o programa:

```bash
python Calculadora.py
```

3. Digite o primeiro número, escolha a operação e o segundo número (se necessário)
4. Digite `sair` a qualquer momento para encerrar o programa

## 📊 Exemplo de Uso

```
--- CALCULADORA ---
Digite 'sair' para encerrar o programa.
Digite o primeiro número: 10
Digite a operação (+, -, *, /, %, sqrt, **, cbrt): +
Digite o segundo número: 5
Resultado: 15
```

Outro exemplo com raiz quadrada:

```
Digite o primeiro número: 16
Digite a operação (+, -, *, /, %, sqrt, **, cbrt): sqrt
Resultado: 4.0
```

## 💡 Conceitos Aprendidos

Este projeto foi desenvolvido com foco em boas práticas Python:

- **Funções modularizadas** para cada operação matemática
- **Tratamento de exceções** com `try/except` e `raise ValueError`
- **Validação de entrada** com tratamento de erros
- **Control flow** com `break` e `continue`
- **Git e versionamento** de código

## 📝 Histórico de Commits

- ✅ Implementação das operações básicas
- ✅ Adição de raiz cúbica, exponenciação e função de saída
- ✅ Adição de operações de porcentagem e raiz quadrada
- ✅ Refatoração com `try/except` e `raise` para melhor tratamento de erros

## 👨‍💻 Autor

Desenvolvido por **Muryllo Augusto**

---

**Feedback e sugestões são bem-vindos!** 🎯
