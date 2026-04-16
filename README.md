# 🏦 Sistema Bancário em Python

Sistema bancário simulado no terminal, desenvolvido em Python com foco em **Programação Orientada a Objetos**. O projeto implementa dois tipos de conta, um painel administrativo e um fluxo completo de cadastro e operações bancárias.

---

## 📋 Funcionalidades

- Cadastro automático de clientes com CPF
- Dois tipos de conta: **Corrente** e **Poupança**
- Operações de depósito, saque e consulta de saldo
- Rendimento mensal de 5% na Conta Poupança
- Taxa de R$10,00 por saque na Conta Corrente
- Painel administrativo para listar e buscar clientes

---

## 🏗️ Estrutura do Projeto

```
banco.py
│
├── Conta              # Classe mãe com atributos e operações base
│   ├── ContaCorrente  # Herda de Conta — cobra R$10 por saque
│   └── ContaPoupanca  # Herda de Conta — possui método render()
│
└── Banco              # Gerencia a lista de clientes
```

---

## ⚙️ Como usar

**Pré-requisitos:** Python 3.6+

```bash
# Clone o repositório
git clone https://github.com/kotinhasslow-crypto/sistema-bancario-python

# Execute o programa
python banco.py
```

**Fluxo de uso:**

1. Digite seu CPF ao iniciar
2. Se for novo: escolha o tipo de conta e faça o cadastro
3. Se já cadastrado: acesse sua conta e realize operações
4. CPF `101` acessa o painel de administrador

---

## 🧱 Classes

### `Conta` — Classe mãe
| Atributo / Método | Descrição |
|---|---|
| `nome`, `cpf`, `tipo` | Dados do titular |
| `_saldo` | Saldo encapsulado |
| `depositar(valor)` | Adiciona valor ao saldo |
| `sacar(valor)` | Remove valor do saldo |
| `ver_saldo()` | Exibe o saldo atual |

### `ContaCorrente(Conta)`
Sobrescreve `sacar()` para cobrar uma taxa fixa de **R$10,00** em cada saque.

### `ContaPoupanca(Conta)`
Adiciona o método exclusivo `render()`, que aplica **5% de rendimento** sobre o saldo.

### `Banco`
| Método | Descrição |
|---|---|
| `adicionar(cliente)` | Cadastra uma conta na lista |
| `listar()` | Exibe todos os clientes |
| `buscar(cpf)` | Busca um cliente pelo CPF |

---

## 💡 Conceitos aplicados

- **Herança** — `ContaCorrente` e `ContaPoupanca` herdam de `Conta`
- **Polimorfismo** — `sacar()` e `depositar()` sobrescritos nas subclasses
- **Encapsulamento** — `_saldo` com prefixo `_` indicando atributo protegido
- **Busca com variável sentinela** — padrão `conta_encontrada = None` para localizar objetos em lista

---

## 🚀 Melhorias futuras

- [ ] Persistência de dados com JSON ou banco de dados
- [ ] Tratamento de erros com `try/except` nas entradas
- [ ] CPF como `str` para suportar zeros à esquerda
- [ ] Interface gráfica ou web com Flask
- [ ] Extrato de transações por conta

---

## 👨‍💻 Autor

Desenvolvido por **Willian** como exercício prático de OOP em Python.
