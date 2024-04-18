from . import welcome_game

ROUNDS_COUNT = 3

def start(game):
    name = welcome_game()
    print(game.DESCRIPTION)
    for _ in range(ROUNDS_COUNT):
        counter = 0
        question, answer = game.generate_round()
        user_answer = input(f'Question: {question}')
        if answer == user_answer:
            counter += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break

    if counter == 3:
        print(f'Congratulations, {name}!')


