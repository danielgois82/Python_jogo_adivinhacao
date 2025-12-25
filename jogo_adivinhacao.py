"""
Jogo onde o computador escolhe um número secreto entre 1 e 20.
O jogador tem 5 tentativas para adivinhar. 
A cada tentativa, o programa informa se o palpite foi muito alto ou muito baixo.
Se o jogador acertar, o loop deve ser interrompido com uma mensagem de vitória.
"""

import os
import random

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho():
    print('-------------------')
    print('Jogo da adivinhação')
    print('-------------------\n')

def main():
    jogar = True

    while jogar:
        numero_secreto = random.randint(1, 20)
        tentativas = 5

        limpar_tela()
        exibir_cabecalho()

        while tentativas > 0:
            numero_digitado = int(input('Digite um número entre 1 e 20: '))
            while numero_digitado not in range(1, 21):
                numero_digitado = int(input('O número deve estar entre 1 e 20, digite outro número: '))

            if numero_digitado == numero_secreto:
                print('\n*** Você advinhou o número, parabens! ***\n')
                break

            tentativas -= 1
            if tentativas >= 1:
                msg = f'Você não advinhou, você tem mais {tentativas} tentativa(s),'
                if numero_secreto > numero_digitado:
                    if numero_secreto - numero_digitado >= 5:
                        print(f'{msg} o palpite foi muito baixo.\n')
                    else:
                        print(f'{msg} o palpite foi baixo.\n')
                    continue

                if numero_secreto < numero_digitado:
                    if numero_digitado - numero_secreto >= 5:
                        print(f'{msg} o palpite foi muito alto.\n')
                    else:
                        print(f'{msg} o palpite foi alto.\n')
                    continue

        if tentativas == 0:
            print(f'\n*** Você perdeu, o número secreto era o {numero_secreto}. ***\n')
        
        opcao = input('Deseja jogar novamente (s/n): ')
        opcao = opcao.lower()
        while opcao not in ('s', 'n'):
            opcao = input('Opção incorreta, deseja jogar novamente (s/n): ')
            opcao = opcao.lower()
        
        jogar = False if opcao == 'n' else True

if __name__ == "__main__":
    main()
