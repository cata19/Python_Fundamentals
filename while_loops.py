# a = 0
# while a < 5:
#     print(f'Hello, {a}')
#     a += 1
# for a in range(5):
#     print(f"Hello, {a}")

user_input = ''

while user_input != '-1':
    user_input = str(input("Guess a number from 1 to 100: "))
    if user_input == 77:
        print("Bingo! you guessed the number")
    print(f"The number is {user_input}. Try again...")
