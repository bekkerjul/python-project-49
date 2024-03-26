def logic(question, correct_answer, points, name):
    print(question)
    answer = int(input())
    if answer == correct_answer:
        return True
    else:
        return f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'\nLet's try again, {name}!"
