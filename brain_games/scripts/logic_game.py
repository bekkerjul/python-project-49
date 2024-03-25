def logic(question, correct_answer):
    print(question)
    answer = int(input())
    if answer == correct_answer:
        return True
    else:
        return False
