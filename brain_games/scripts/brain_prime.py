from .brain_games import welcome_game
from ..cly import welcome_user
from random import randint
from .logic_game import logic

def is_prime(num):
    dividers = []

    for elem in range(1, num + 1):
        if num % elem == 0:
            dividers.append(elem)

    if len(dividers) == 2:
        return 'yes'
    else:
        return 'no'


def brain_prime():
    name = welcome_game()
    points = 0
    question = f'Answer "yes" if given number is prime. Otherwise answer "no".'

    while points < 3:
        num = randint(1, 100)
        print(f'Question: {num}')
        correct_answer = is_prime(num)
        flag = logic(question, correct_answer, points, name)

        if flag == True:
            points += 1
        else:
            print(flag)
            break

    if points == 3:
        print(f'Congratulations, {name}!')


def main():
    brain_prime()

if __name__ == '__main__':
    main()
