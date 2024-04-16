from random import randint


def even_game():
    question = 'Answer "yes" if the number is even, otherwise answer "no".'
    num = randint(0, 10000000)
    answer = int(input('Your answer: '))
    correct_answer = num % 2

    if (correct_answer == 1 and answer == 'no') or (correct_answer == 0 and answer == 'yes'):
        flag = True
    else:
        flag = False

    return [question, flag, answer, correct_answer]


def main():
    even_game()


if __name__ == '__main__':
    main()
