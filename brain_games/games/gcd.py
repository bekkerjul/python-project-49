from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    question = f'{num1} {num2}'
    gsd1 = set([i for i in range(num1) if num % i == 0 else 1])
    gsd2 = set([i for i in range(num2) if num % i == 0 else 1])
    answer = max(list(find_gcd(num1) & find_gcd(num2)))
    return question, str(answer)


