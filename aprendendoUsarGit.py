from calculadora.operacoes_simlples import somar, subtracao

if __name__ == '__main__':
    opcao = -1
    while opcao != 3:
        print('Calculadora Git')
        print("=" * 20)
        print('1 - Somar')
        print('2 - Subtração')
        print('3 - Sair')
        print("=" * 20)
        opcao = int(input("Opção: "))

        if opcao == 1:
             operador1 = int(input("Digite o numero que deseja somar: "))
             operador2 = int(input("Digite outro numero para concluir a soma: "))
             somar(operador1, operador2)
             resultado = somar(operador1, operador2)
             print(f'Soma: {resultado}')
             print()
        elif opcao == 2:
             operador1 = int(input("Digite o numero que deseja subtrair: "))
             operador2 = int(input("Digite outro numero para concluir a subtração: "))
             subtracao(operador1, operador2)
             resultado = subtracao(operador1, operador2)
             print(f'Subtração: {resultado}')
             print()
             
             
        elif opcao == 3:
             print('Obrigado por usar a nossa calculadora')
