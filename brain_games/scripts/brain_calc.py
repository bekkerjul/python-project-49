from random import randint, choice


def brain_calc():
    question = 'What is the result of the expression?'
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        operator = choice(['+', '-', '*'])
        answer = int(input('Your answer: '))

        if operator == '+':
            correct_answer = sum([num1, num2])
        elif operator == '-':
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2

        if answer == correct_answer:
            flag = True
        else:
            flag = False

    return [question, flag, answer, correct_answer]


def main():
    brain_calc()


if __name__ == '__main__':
    main()
