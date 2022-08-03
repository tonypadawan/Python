import random
import os


# variables
secret_number = random.randint(1, 100)
attempts = 0  # Tentativas
lifes = 0
points = 500
test_level = 1


print('+-' * 17)
print(' Welcome ao jogo da Adivinhação!')
print('+-' * 17 )
print()

while test_level == 1:
    level = int(input('Escolha a dificuldade: [ 1 - Fácil, 2 - Normal, 3 - Difícil ] : '))

    if level < 1 or level > 3:
        print('Valor invalido! Escolha entre 1 e 3. \n')

    elif level == 1:
        lifes = 12
        test_level = 0

    elif level == 2:
        lifes = 8
        test_level = 0

    else:
        lifes = 5
        test_level = 0

os.system('clt' if os.name == 'nt' else 'clear')


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

    hit = kick_number == secret_number  # Acertou
    less = kick_number < secret_number  # Menor

    # Limpa a tela;
    os.system('cls' if os.name == 'nt' else 'clear') 
    
    
    if hit:
        break

    elif less:
        print(f'Você errou! {kick_number} é MENOR que o número secreto! \n')
        points -= (secret_number - kick_number) / 2

    else:
        print(f'Você errou! {kick_number} é MAIOR que o número secreto! \n')
        points -= (kick_number - secret_number) / 2
    
    print()


if hit:
    print(f'Parabéns, Você acertou! O número secreto era {secret_number}.')

else:
    print(f'Que pena, você perdeu! O número secreto era {secret_number}.')
    print('Tente novamente! \n')


print(f'Você fez {points} pontos! \n')
print('Game-Over')
