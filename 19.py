def jogo_adivinhacao(numero_secreto):
    while True:
        palpite = int(input("Digite seu palpite: "))
        if palpite == numero_secreto:
            print("Parabéns! Você acertou!")
            break
        elif palpite > numero_secreto:
            print("Maior que o número secreto.")
        else:
            print("Menor que o número secreto.")
