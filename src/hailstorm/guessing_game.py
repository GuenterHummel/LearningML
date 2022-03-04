import random


def guessing_game():
    answer = random.randint(0, 100)

    while True:
        user_input = input('What is your guess? ')

        if user_input.isdigit():
            user_guess = int(user_input)

            if user_guess == answer:
                print(f'Right! The answer is {user_guess}')
                break

            if user_guess < answer:
                print(f'Your guess of {user_guess} is too low!')
            else:
                print(f'Your guess of {user_guess} is too high!')
        else:
            print(f'Your input of {user_input} is no number, please retry')


guessing_game()
