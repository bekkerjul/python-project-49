from random import randint
from .brain_games import welcome_game
from ..cly import welcome_user

def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'

def even_game():
    name = welcome_user()
    points = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while points < 3:
        num = randint(0, 10000000)
        print(f'Question: {num}')
        answer = input('Your answer: ')
        right_answer = is_even(num)
        if answer == right_answer:
            print('Correct!')
            points += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
            points = 0

    print(f'Congratulations, {name}!')

def main():
    even_game()

if __name__ == '__main__':
    main()
