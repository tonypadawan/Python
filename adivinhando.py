import random
import os


# variables
secret_number = random.randint(1, 100)
attempts = 0  # Tentativas
lifes = 0
points = 500


def verification_values(value):
   num_test = 1

   if value == 'K':
        print(f'Tentativa {attempts} de {lifes} \n')

        while num_test == 1:
            value = int(input('Chuta um número entre 1 e 100: '))

            if value <= 0 or value > 100:
                print('Chute inválido! Valor informado é zero ou negativo! \n')
            else:
                num_test = 0
                return value
        

   elif value == 'L':
       while num_test == 1:
           value = int(input('Escolha a dificuldade: [ 1 - Fácil, 2 - Normal, 3 - Difícil ] : '))

           if value < 1 or value > 3:
                print('Valor inválido! Escolha entre 1 e 3! \n')
            
           else:
                num_test = 0
                return value
       

print('+-' * 17)
print(' Welcome ao jogo da Adivinhação!')
print('+-' * 17 )
print()

level = verification_values('L')

if level == 1:
    lifes = 12
       
elif level == 2:
    lifes = 8
        
else:
    lifes = 5


os.system('clt' if os.name == 'nt' else 'clear')


for attempts in range(1, lifes + 1):

    kick_number = verification_values('K')

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
