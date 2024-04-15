from random import randint
from ..cly import welcome_user


def is_even():
    num = randint(0, 10000000)
    print(f'Question: {num}')
    answer = int(input('Your answer: '))
    return 'yes' if answer % 2 == 0 else 'no', answer


def even_game():
    question = 'Answer "yes" if the number is even, otherwise answer "no".'
    is_even()

        num = randint(0, 10000000)
        print(f'Question: {num}')
        answer = input('Your answer: ')
        right_answer = is_even(num)
        if answer == right_answer:
            print('Correct!')
            points += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break

    if points == 3:
        print(f'Congratulations, {name}!')


def main():
    even_game()


if __name__ == '__main__':
    main()
