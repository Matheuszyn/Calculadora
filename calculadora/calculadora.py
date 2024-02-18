from math import sqrt
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opçao = 0
while opçao != 10:
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
    [ 8 ] Raiz quadrada
    [ 9 ] Novos números
    [ 10 ] Sair do programa''')
    opçao = int(input('>>>>> Qual é a sua opção: '))
    if opçao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif opçao == 2:
        subtraçao = n1 - n2
        print(f'A subtração entre {n1} - {n2} é {subtraçao}')
    elif opçao == 3:
        mult = n1 * n2
        print(f'A multiplicação entre {n1} x {n2} é {mult}')
    elif opçao == 4:
        divisao = n1 / n2
        print(f'A divisão entre {n1} / {n2} é {divisao:.1f}')
    elif opçao == 5:
        modulo = n1 % n2 
        print(f'O resto da divisão entre {n1} % {n2} é {modulo}')
    elif opçao == 6:
        print('''
        [ 1 ] Percentual da soma dos valores
        [ 2 ] Mesmo percentual para os dois valores separadamente
        [ 3 ] Digitar um novo valor''')
        escolha = int(input('Sua escolha: '))
        if escolha == 1:
            porcentagem = int(input('Digite a porcentagem desejada: '))
            soma = n1 + n2
            resultado = soma * (porcentagem / 100)
            print(f'{porcentagem}% de {soma} é {resultado}')
        elif escolha == 2:
            porcentagem1 = int(input(f'Digite a porcentagem desejada para {n1}: '))
            porcentagem2 = int(input(f'Digite a porcentagem desejada para {n2}: '))
            resultado1 = n1 * (porcentagem1 / 100)
            resultado2 = n2 * (porcentagem2 / 100)
            print(f'{porcentagem1}% de {n1} é {resultado1:.2f}, e {porcentagem2}% de {n2} é {resultado2:.2f}')
        elif escolha == 3:
            n3 = int(input('Digite um novo valor: '))
            porcentagem = int(input('Digite a porcentagem desejada: '))
            resultado = n3 * (porcentagem / 100)
            print(f'{porcentagem}% de {n3} é igual a {resultado}')
    elif opçao == 7:
        potencia = n1 ** n2
        print(f'A potência entre {n1} ** {n2} é {potencia}')
    elif opçao == 8:
        print('''
        [ 1 ] Raiz quadrada da soma dos valores
        [ 2 ] Raiz quadrada dos dois valores separadamente
        [ 3 ] Digitar um novo valor''')
        escolha = int(input('Sua escolha: ')) 
        if escolha == 1:
            soma = n1 + n2
            raiz = sqrt(soma)
            print(f'A raiz quadrada de {soma} é {raiz}')
        elif escolha == 2:
            raiz1 = sqrt(n1)
            raiz2 = sqrt(n2)
            print(f'A raiz quadrada de {n1} é {raiz1}, e a de {n2} é {raiz2}') 
        elif escolha == 3:
            n3 = int(input('Digite um novo valor: '))
            raiz = sqrt(n3)
            print(f'A raiz quadrada de {n3} é {raiz}')
    elif opçao == 9:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opçao == 10:
        print('Finalizando...')
    else: 
        print('Opção inválida. Tente novamente.')
    sleep(2)

print('Fim do programa! Volte sempre!!!')