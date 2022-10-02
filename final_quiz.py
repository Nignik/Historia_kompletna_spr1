import random
from tasks import questions_map


def questions_answers():
    subject = random.choice(list(questions_map.values()))
    subject = random.choice(subject)
    question = subject.question
    player_answer = input(question)
    print(f"Odpowiedz wzorcowa: {subject.answer}")
    return player_answer


def info():
    player_question = input("O czym chcesz sie dowiedziec kolego?\n")
    if player_question in questions_map:
        iterator = questions_map[player_question]
        for obj in iterator:
            print(obj.question)
            print(obj.answer)
    else:
        print("Niestety nie ma takiego wpisu w bazie danych")
    return input("Do you want to quit?\n Type: 'koniec' to end\n")


def play_final_quiz():
    info_or_question = input("Chcesz grac w Q&A, czy chcesz otrzymac informacje:\n'a': Q&A\n'b':Informacje\n")
    player_answer = ""
    while player_answer != "koniec":

        if info_or_question == "a":
            player_answer = questions_answers()
        elif info_or_question == "b":
            player_answer = info()
