from .brain_games import welcome_game
from random import randint
from .logic_game import logic


def find_gcd(num):
    gcds = set()
    for elem in range(1, num + 1):
        if num % elem == 0:
            gcds.add(elem)
    return gcds


def brain_gcd():
    name = welcome_game()
    points = 0
    question = 'Find the greatest common divisor of given numbers.'

    while points < 3:
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        print(f'Question: {num1} {num2}')
        correct_answer = max(list(find_gcd(num1) & find_gcd(num2)))
        flag = logic(question, correct_answer, points, name)
        if flag is True:
            points += 1
        else:
            print(flag)
            break

    if points == 3:
        print(f'Congratulations, {name}!')


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
