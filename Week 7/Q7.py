questions = [
    "Which keyword defines a function?",
    "Which symbol starts a comment",
    "Which data type stores true or false"
]

answers = ["def","#","bool"]

def run_quiz(questions,answers):
    score = 0
    for i in range(len(questions)):
        reply = input(questions[i] + " ")
        reply = reply.strip().lower()

        if reply == answers[i].lower():
            print("Bingo!")
            score += 1
        else:
            print("Wrong! The right answer is", answers[i])
    return score

whats_left = questions[1:]
print("Questions left:")
for q in whats_left:
    print("-",q)
print()

play_again = "yes"
while play_again == "yes":
    score = run_quiz(questions,answers)
    print("Your score:", score)
    play_again = input("Play again? Yes/No: ").strip().lower()

print("Play again sometime? Please come back")