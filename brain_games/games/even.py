from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    question = randint(0, 10000000)
    answer = 'yes' if question % 2 == 0 else 'no'
    return str(question), answer
