from .brain_games import welcome_game
from ..cly import welcome_user
from random import randint, choice

def brain_calc():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    name = welcome_user()
    points = 0

    print('What is the result of the expression?')
    operator = choice(['+', '-', '*'])

    while points < 3:
        print(f'Question: {num1} {operator} {num2}')

        if operator == '+':
            correct_answer = sum([num1, num2])
        elif  operator == '-':
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2

        answer = int(input('Your answer: '))

        if answer == correct_answer:
            points += 1
            print(f'Correct!')
        else:
            points = 0
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'\nLet's try again, {name}!")

    print(f'Congratulations, {name}')
