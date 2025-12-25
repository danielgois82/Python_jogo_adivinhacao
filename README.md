# Jogo da Adivinhação – Python via Terminal CLI

Um simples e divertido **jogo de adivinhação** desenvolvido em Python, onde o **computador escolhe um número secreto entre 1 e 20** e o jogador tem **5 tentativas** para acertar.
A cada palpite, o jogo informa se o número digitado foi **alto, baixo, muito alto ou muito baixo**, além de permitir jogar novamente quantas vezes quiser.

---

## 🎯 Objetivo deste Jogo

Treinar a linguagem de programação **Python**, utilizando conceitos como:

* Estruturas de repetição
* Condicionais
* Funções
* Geração de números aleatórios
* Interação via terminal

---

## 🚀 Funcionalidades

* Geração aleatória de um número secreto entre 1 e 20
* Limite de 5 tentativas por rodada
* Validação de entrada (aceita apenas números entre 1 e 20)
* Feedback a cada tentativa (alto, baixo, muito alto ou muito baixo)
* Mensagem de vitória ou derrota
* Opção de jogar novamente (`s` para sim, `n` para não)
* Limpeza da tela a cada nova partida

---

## 🧠 Regras do Jogo

* O computador escolhe um número secreto entre **1 e 20**
* O jogador tem **5 tentativas** para acertar
* A cada erro, o jogo informa se o palpite foi:

  * **Muito baixo**
  * **Baixo**
  * **Alto**
  * **Muito alto**
* Se o jogador acertar, o jogo termina com mensagem de vitória
* Se as tentativas acabarem, o número secreto é revelado

---

## 📦 Pré-requisitos

* Python 3 instalado
* Terminal / Prompt de Comando

---

## ▶️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/Python_jogo_adivinhacao.git
```

2. Acesse a pasta do projeto:

```bash
cd Python_jogo_adivinhacao
```

3. Execute o script:

```bash
python jogo_adivinhacao.py
```

---

## 🧩 Código

O algoritmo funciona em um loop que:

1. Gera um número secreto aleatório
2. Solicita um número ao jogador
3. Valida se o número está entre 1 e 20
4. Compara o palpite com o número secreto
5. Exibe dicas ao jogador
6. Controla o número de tentativas
7. Pergunta se o jogador deseja jogar novamente

---

## 🖥️ Exemplo de uso

```
-------------------
Jogo da adivinhação
-------------------

Digite um número entre 1 e 20: 10
Você não advinhou, você tem mais 4 tentativa(s), o palpite foi baixo.

Digite um número entre 1 e 20: 15
Você não advinhou, você tem mais 3 tentativa(s), o palpite foi alto.

Digite um número entre 1 e 20: 14

*** Você advinhou o número, parabéns! ***

Deseja jogar novamente (s/n):
```

---

## 📜 Licença

Este projeto é de uso livre.
Sinta-se à vontade para estudar, modificar, melhorar e reutilizar!

---