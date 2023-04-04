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
             print('Opção somar')
        elif opcao == 2:
             print('Opção Subtração')
             
        elif opcao == 3:
             print('Obrigado por usar a nossa calculadora')
