from random import randint
from .logic_game import logic
from .brain_games import welcome_game


def progression():
    name = welcome_game()
    points = 0

    while points < 3:
        first_num = randint(1, 10)
        step = randint(1, 10)
        len_pogression = randint(5, 15)
        random_index = randint(0, len_pogression)
        progression_list = []

        for num in range(first_num, len_pogression + 1, step):
            progression_list.append(num)

        correct_answer = progression_list[random_index]
        progression_list[random_index ] = '..'
        question = f'Question: {*progression_list}'
        print(question)
        flag = logic(question, correct_answer, points, name)

        if flag == True:
            points += 1
        else:
            print(flag)

    print(f'Congratulations, {name}')


def main():
    progression()

if name == 'main':
    main()
