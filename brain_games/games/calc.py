from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operator = choice(['+', '-', '*'])
    question = f'{num1} {operator} {num2}'

    if operator == '+':
        answer = sum([num1, num2])
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return question, answer


