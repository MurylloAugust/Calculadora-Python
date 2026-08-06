# Calculadora Científica Python CLI 🧮

Uma calculadora de linha de comando (CLI) desenvolvida em Python, com foco em boas práticas de programação, tratamento de exceções, modularização e expansão para funções científicas avançadas.

---

## 🚀 Funcionalidades Atuais

- **Operações Básicas**:
  - Soma (`+`)
  - Subtração (`-`)
  - Multiplicação (`*`)
  - Divisão (`/`) com validação contra divisão por zero
  - Porcentagem (`%`)
- **Potenciação e Raízes**:
  - Exponenciação (`**`)
  - Raiz Quadrada (`sqrt`) com validação para números negativos
  - Raiz Cúbica (`cbrt`) com suporte a números negativos
- **Usabilidade e Tratamento de Erros**:
  - Comando de saída (`sair`) funcional em qualquer etapa sem interromper o programa abruptamente.
  - Tratamento de entradas com `.strip().lower()` para evitar erros com espaços extras ou letras maiúsculas.
  - Validação de dados via `try/except` (`ValueError`) contra digitações inválidas.

---

## 📌 Próximas Funcionalidades (Roadmap)

Planejadas para as próximas versões da calculadora:

- [ ] **Trigonometria**: Seno (`sin`), Cosseno (`cos`), Tangente (`tan`)
- [ ] **Trigonometria Inversa / Hiperbólica**: ArcSen, ArcCos, ArcTan, Sinh, Cosh, Tanh
- [ ] **Logaritmos**: Logaritmo natural (`ln`), Logaritmo na base 10 (`log10`), Logaritmo em base arbitrária
- [ ] **Constantes Matemáticas**: Integração de $\pi$ (Pi) e $e$ (Número de Euler)
- [ ] **Fatorial e Combinatória**: Fatorial (`n!`), Permutações e Combinações
- [ ] **Conversão de Ângulos**: Suporte a Graus e Radianos

---

## 🛠️ Pré-requisitos

- **Python 3.x** instalado (utiliza a biblioteca nativa `math` para funções científicas).

---

## 🔧 Como Executar

1. **Clone o repositório**:
   ```bash
   git clone [https://github.com/seu-usuario/Calculadora-Python.git](https://github.com/seu-usuario/Calculadora-Python.git)
   cd Calculadora-Python
