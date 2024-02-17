n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opçao = 0
while opçao != 11:
    print('=' * 20)
    print('{:^20}'.format('MENU'))
    print('=' * 20)
    print('''
    [ 1 ] Adição
    [ 2 ] Subtração
    [ 3 ] Multiplicação
    [ 4 ] Divisão
    [ 5 ] Módulo
    [ 6 ] Porcentagem
    [ 7 ] Potenciação
    [ 8 ] Fatorial
    [ 9 ] Raiz quadrada
    [ 10 ] Novos números
    [ 11 ] Sair do programa''')
    opçao = int(input('>>>>> \033[32mQual é a sua opção: \033[m')).strip()
    