def logic(question, correct_answer, points, name):
    print(question)
    answer = input()
    if answer.isdigit() or answer[1:].isdigit():
        answer = int(answer)
    if answer == correct_answer:
	return True
    else:
        print(f"'{answer}' is wrong answer ;(.", end=' ')
        print(f"Correct answer was '{correct_answer}'")
        print(f"Let's try again, {name}!")
