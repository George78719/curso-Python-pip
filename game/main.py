# JUEGO:  PIEDRA PEPEL O TIJERA
import random

def choose_options():
    opciones = ('piedra', 'papel', 'tijera')
    user_option = input('\nPiedra, pepel o tijera = ')
    user_option = user_option.lower()

    if not user_option in opciones:
        print('esa opcion no es valida')
        return None, None

    computer_option = random.choice(opciones) # Selección de opción aleatoria del computador

    print('User Option => ', user_option)
    print('Computer option => ', computer_option)

    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('User gano!')
            user_wins +=1
        else:
            print('Papel gana a piedra:')
            print('Computer gano!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra')
            print('User gano!')
            user_wins += 1
        else:
            print('Tijera caja a papel')
            print('Computer gano!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a papel')
            print('User gano!')
            user_wins += 1
        else:
            print('Piedra gana a tijera')
            print('Computer gano!')
            computer_wins += 1
    
    return user_wins, computer_wins


def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print('\n')
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        print('computer_wins ', computer_wins)
        print('user_wins ', user_wins)

        user_option, computer_option = choose_options()

        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)


        if computer_wins == 2:
            print("\nEl ganador es la computadora!")
            break
        if user_wins == 2:
            print("\nEl ganador es el usuario!")
            break

        rounds += 1

run_game()