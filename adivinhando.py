# variables
secret = 38
lifes = 3
attempts = 0  # Tentativas

print('+-' * 17)
print(' Welcome ao jogo da Adivinhação!')
print('+-' * 17)

for attempts in range(1, lifes + 1):

    invalid_number = 1
    kick_number = 0

    print(f'Tentativa {attempts} de {lifes} \n')

    while invalid_number == 1:
        kick_number = int(input('Chuta um número entre 1 e 100: '))

        if kick_number <= 0 or kick_number > 100:
            print('Valor inválido! O número é NEGATIVO ou maior que 100!')
        else:
            invalid_number = 0

    print()

    hit = kick_number == secret  # Acertou
    less = kick_number < secret  # Menor

    if hit:
        print('Parabéns, Você acertou! \n')
        break

    elif less:
        print(f'Você errou! {kick_number} é MENOR que o número secreto! \n')

    else:
        print(f'Você errou! {kick_number} é MAIOR que o número secreto! \n')

print('Game-Over')
