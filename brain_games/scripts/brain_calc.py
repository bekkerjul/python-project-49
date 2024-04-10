from .brain_games import welcome_game
from ..cly import welcome_user
from random import randint, choice
from .logic_game import logic

def brain_calc():
    name = welcome_game()
    points = 0

    question = 'What is the result of the expression?'

    while points < 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        operator = choice(['+', '-', '*'])
        print(f'Question: {num1} {operator} {num2}')

        if operator == '+':
            correct_answer = sum([num1, num2])
        elif  operator == '-':
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2

        flag = logic(question, correct_answer, points, name)

        if flag == True:
            points += 1
        else:
            print(flag)
            break

    if points == 3:
        print(f'Congratulations, {name}!')


def main():
    brain_calc()

if __name__ == '__main__':
    main()
