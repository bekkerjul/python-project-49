from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    question = randint(1, 100)
    dividers = []
    for num in range(1, question + 1):
        dividers.append(num) if question % num == 0 else False
    answer = 'yes' if len(dividers) == 2 else 'no'
    return str(question), answer
