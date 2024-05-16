
while True:

    print("calculadora cancelada:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("X - Sair")

    opcao = input("Qual sua escolha?: ").strip().upper()

    if opcao == 'X':
        print("Encerrando a calculadora.")
        break

    if opcao not in ('1', '2', '3', '4'):
        print("Opção inválida! Tente novamente.")
        continue

    numeros = []

    while True:
        entrada = input("Digite um número (ou 'P' para processar): ").strip().upper()

        if entrada == 'P':
            break

        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida! Digite um número ou 'P'.")

    if numeros:
        resultado = numeros[0]
        if opcao == '1':
            for num in numeros[1:]:
                resultado += num
        elif opcao == '2':
            for num in numeros[1:]:
                resultado -= num
        elif opcao == '3':
            for num in numeros[1:]:
                resultado *= num
        elif opcao == '4':
            for num in numeros[1:]:
                if num == 0:
                    print("Erro: Divisão por zero!")
                    break
                resultado /= num

        print("Resultado da operação é:", resultado)
    else:
        print("Nenhum número foi digitado!")
