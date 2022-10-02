import final_quiz
import os
import dates_quiz

print("Kórżóchś")
while 0 == 0:
    game = input("What do you want to play:\n'a': Postacie\n'b': Daty\n")

    while game == 'a':
        os.system('cls')
        final_quiz.play_final_quiz()
        game = ""

    while game == 'b':
        os.system('cls')
        dates_quiz.play_dates_quiz()
        game = ""
