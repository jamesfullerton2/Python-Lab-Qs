grade = 75
# grade = 40
# grade = 25

def check_result(mark):
    if mark >= 70:
        print("Excellent!")

    elif mark >=40:
        print("You passed")

    else:
        print("You failed...")

print(check_result(grade))