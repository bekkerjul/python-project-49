def logic(question, correct_answer, points):
    print(question)
    answer = int(input())
    if answer == correct_answer:
        points += 1
        return points
    else:
        return f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'\nLet's try again, {name}!"
