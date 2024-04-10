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
        progression_list = []
        print(f'What number is missing in the progression?')

        for i in range(0, len_pogression):
            progression_list.append(0)

        progression_list[0] = first_num

        for i in range(1, len_pogression):
            progression_list[i] = progression_list[i - 1] + step

        random_index = randint(0, len_pogression - 1)
        correct_answer = progression_list[random_index]
        progression_list[random_index] = '..'
        question = f'Question: {" ".join(map(str, progression_list))}'
        flag = logic(question, correct_answer, points, name)

        if flag == True:
            points += 1
        else:
            print(flag)
            break

    if points == 3:
        print(f'Congratulations, {name}!')


def main():
    progression()

if __name__ == '__main__':
    main()
