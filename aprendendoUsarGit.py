if __name__ == '__main__':
    opcao = -1
    while opcao != 2:
        print('Calculadora Git')
        print("=" * 20)
        print('1 - Somar')
        print('2 - Sair')
        print("=" * 20)
        opcao = int(input("Opção: "))

        if opcao == 1:
             print('opção somar')
        elif opcao == 2:
             print('Obrigado por usar a nossa calculadora')
