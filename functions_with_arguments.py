def greeting(name):
    print(f"Hello, {name}!")


greeting("Ibrahim")


def user_guessing_game(secret_number):
    user_input = ''
    while user_input != int('-1'):
        user_input = int(input('Guess a number from 1 to 100: '))
        if user_input == secret_number:
            print('Bingo! You guessed the number')
        else:
            print(f"The number is {user_input}. Try again...")


user_guessing_game(99)
