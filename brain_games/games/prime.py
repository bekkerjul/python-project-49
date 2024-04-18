from random import randint

DESRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    question = randint(1, 100)
    gsd = len([i for i in range(1, question + 1) if question % i == 0 else False])
    answer = 'yes' if gsd == 2 else 'no'
    return str(question), answer

