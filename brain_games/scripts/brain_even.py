from random import randint
from ..cly import welcome_user


def is_even():
    num = randint(0, 10000000)
    print(f'Question: {num}')
    answer = int(input('Your answer: '))
    correct_answer = num % 2

    if (correct_answer == 1 and answer == 'no') or (correct_answer == 0 and answer == 'yes'):
        return True, answer, correct_answer
    else:
        return False,answer, correct_answer


def even_game():
    question = 'Answer "yes" if the number is even, otherwise answer "no".'
    flag, answer, correct_answer = is_even()
    return question, flag, answer, correct_answer


def main():
    even_game()


if __name__ == '__main__':
    main()
