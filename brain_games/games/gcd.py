from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def find_divisors(num):
    divisors_list = []
    for n in range(1, num + 1):
        divisors_list.append(n) if num % 2 == 0 else False
    return set(divisors_list)


def generate_round():
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    question = str(num1) + ' ' + str(num2)
    answer = max(list(find_divisors(num1) & find_divisors(num2)))
    return question, str(answer)

