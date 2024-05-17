import sys
import os

def positivo_nulo_negativo(num):
    if num > 0:
        tipo = 'Valor Positivo'
    elif num < 0:
        tipo = 'Valor Negativo'
    else:
        tipo = 'Valor Nulo'
    return tipo


def valor_absoluto(num):
    if num < 0:
        return num * -1
    else:
        return num


def fatorial(num, cal=False):

    # Se o número for 0
    if num == 0:
        return 1

    # Se o número for negativo
    elif num < 0:

        # Trocando o sinal, número negativo não tem fatorial
        print('\033[1;30;41mNão existe fatorial de número negativo!\033[m')
        num *= -1

    print(f'\033[30;42mFazendo fatorial do número {num}...\033[m')

    # Mostrar o número inicial caso váriavel 'cal' for igual a True
    if cal:
        print('\033[30;42m', num, end=' * ')

    # Calculo de fatorial
    for fat in range(num - 1, 0, -1):
        # Mostrar cálculo caso váriavel 'cal' for True
        if cal:
            if fat == 1:
                print(fat, end=' = ')
            else:
                print(fat, end=' * ')
        # Resposta
        num *= fat
    return num


def menus(num=0):
    # Caso interrompido pelo usuario usa tratamento de erro
    try:

        # Loop do menu
        while True:
            print(f'\033[4;30;44m{"MENU":^25}\033[m')
            print(f'\033[1;30;45m{f"Número atual: {num}":^25}\033[m')
            print('\033[1;30;44m-\033[m' * 25)

            # Menu
            for menu in range(1, 6):
                opc = ''
                if menu == 1:
                    opc = 'Tipo de número(+/-)'
                elif menu == 2:
                    opc = 'Valor Absoluto'
                elif menu == 3:
                    opc = 'Fatorial'
                elif menu == 4:
                    opc = 'Trocar número'
                elif menu == 5:
                    opc = 'Sair'
                print(f'\033[1;30;44m{f"[ {menu} ] {opc}":<25}\033[m')

            # Loop de verificação da escolha
            while True:
                print('\033[1;30;44m-\033[m' * 25)

                # Loop de verificação se é um número inteiro
                while True:
                    escolha = str(input(f'\033[1;30;43m{"Opção:":^25}\033[m')).strip()
                    print('\033[1;30;44m-\033[m' * 25)

                    # Se for número inteiro, transforma em int e finaliza esse loop.
                    if escolha.isnumeric():
                        escolha = int(escolha)
                        break

                    # Se não for, mostra uma mensagem e o menu novamente
                    else:
                        print('\033[1;30;41mEscolha uma opção válida!\033[m')
                        print('\033[1;30;44m-\033[m' * 25)

                        # Menu
                        for menu in range(1, 6):
                            opc = ''
                            if menu == 1:
                                opc = 'Tipo de número(+/-)'
                            elif menu == 2:
                                opc = 'Valor Absoluto'
                            elif menu == 3:
                                opc = 'Fatorial'
                            elif menu == 4:
                                opc = 'Trocar número'
                            elif menu == 5:
                                opc = 'Sair'
                            print(f'\033[1;30;44m{f"[ {menu} ] {opc}":<25}\033[m')

                # Verifica se o número é uma opção válida (1 a 5)
                if 0 < escolha < 6:
                    break

                # Se não for, mostra uma mensagem e o menu novamente
                else:
                    print('\033[1;30;44m-\033[m' * 25)
                    print('\033[1;30;41mEscolha uma opção válida!\033[m')
                    print('\033[1;30;44m-\033[m' * 25)

                    # Menu
                    for menu in range(1, 6):
                        opc = ''
                        if menu == 1:
                            opc = 'Tipo de número(+/-)'
                        elif menu == 2:
                            opc = 'Valor Absoluto'
                        elif menu == 3:
                            opc = 'Fatorial'
                        elif menu == 4:
                            opc = 'Trocar número'
                        elif menu == 5:
                            opc = 'Sair'
                        print(f'\033[1;30;44m{f"[ {menu} ] {opc}":<25}\033[m')

            # Primeira opção do menu
            if escolha == 1:
                print(f'\033[30;42m{positivo_nulo_negativo(num):^25}\033[m')
                print('\033[1;30;44m-\033[m' * 25)

            # Segunda opção do menu
            elif escolha == 2:
                print(f'\033[30;42m{f"Valor absoluto de {num}: {valor_absoluto(num)}":^25}\033[m')
                print('\033[1;30;44m-\033[m' * 25)

            # Terceira opção do menu
            elif escolha == 3:

                # Loop de verificação da resposta
                while True:
                    while True:
                        if num == 0:
                            cal = 'N'
                        else:
                            cal = str(input('\033[30;43mMostrar cálculo? [SIM/NÃO]\033[m')).strip()

                        # Verificar se algo foi escrito
                        if len(cal) > 0:

                            # Armazena o primeiro valor colocado em maiúsculo (ex: 'sim' cal = [S])
                            cal = cal.upper()[0]
                            break

                        # Mensagem de erro
                        else:
                            print('\033[1;30;41mPorfavor responda com sim ou não!\033[m')

                    # Verifica se foi escolhido sim ou não e faz seu comando.
                    if cal == 'S':
                        print(f"{fatorial(num, True)}", end='\033[m\n')
                        break
                    elif cal == 'N':
                        print(f'\033[30;42m{fatorial(num):^25}\033[m')
                        break

                    # Mensagem de erro
                    else:
                        print('\033[1;30;41mPorfavor responda com sim ou não!\033[m')
                print('\033[1;30;44m-\033[m' * 25)

            # Quarta opção do menu
            elif escolha == 4:

                # Loop de verificação do número
                while True:

                    # Retirar espaços antes e depois
                    numero = str(input(f'\033[1;30;43m{"Informe o novo valor:":^25}\033[m')).strip()
                    print('\033[1;30;44m-\033[m' * 25)

                    # Verificar se é tudo número, se sim faz a alteração
                    # .raplace permite substitui negativo por vazio para verificar (ex: -45 ¬> 45)
                    if numero.replace('-', '').isnumeric():
                        print(f'\033[4;30;45mNúmero {numero} lido e alterado com sucesso.\033[m')
                        num = int(numero)
                        break
                    else:
                        print(f'\033[1;30;41mPorfavor digite um número inteiro válido.\033[m')
                        print('\033[1;30;44m-\033[m' * 25)

            # Quinta opção do menu
            elif escolha == 5:
                print(f'\033[1;30;41m{"Até a próxima":^25}\033[m')
                break

    # Mensagem para interrupção do código
    except KeyboardInterrupt:
        print(f'\n\033[1;30;41m{"Até a próxima":^25}\033[m')
        
        # Não aparecer o erro direcionando para um arquivo vazio
        sys.stderr = open(os.devnull, 'w')


if __name__ == '__main__':
    menus()
