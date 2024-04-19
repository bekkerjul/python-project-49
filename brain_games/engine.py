from brain_games.scripts.brain_games import welcome_game

ROUNDS_COUNT = 3


def start(game):
    name = welcome_game()
    print(game.DESCRIPTION)
    counter = 0
    for _ in range(ROUNDS_COUNT):
        question, answer = game.generate_round()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if answer == user_answer:
            counter += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."\\\
                  f"Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break

    if counter == 3:
        print(f'Congratulations, {name}!')
