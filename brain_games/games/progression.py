from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def generate_round():
    first_num = randint(1, 10)
    step = randint(1, 10)
    len_pogression = randint(5, 15)
    progression_list = []

    for i in range(0, len_pogression):
        progression_list.append(0)

    progression_list[0] = first_num

    for i in range(1, len_pogression):
        progression_list[i] = progression_list[i - 1] + step

    random_index = randint(0, len_pogression - 1)
    answer = progression_list[random_index]
    progression_list[random_index] = '..'
    question = " ".join(map(str, progression_list))
    return question, str(answer)

