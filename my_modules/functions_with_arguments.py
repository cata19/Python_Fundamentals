def greeting(name):
    print(f"Hello, {name}!")


name = 'Alice'


class Test:
    a = 55


def user_guessing_game(secret_number, stop_chars):
    user_input = ''
    while user_input != stop_chars:
        user_input = input('\nGuess a number from 1 to 100: ')
        if user_input == secret_number:
            print('Bingo! You guessed the number')
        else:
            print(f"The number is {user_input}. Try again...")
