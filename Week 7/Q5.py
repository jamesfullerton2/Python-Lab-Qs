with open("Week 7/Lab Qs/marks.txt", "w") as marks:
    marks.write("65\n")
    marks.write("72\n")
    marks.write("48\n")

mark_list = []

with open("Week 7/Lab Qs/marks.txt","r") as marks:
    for line in marks:
        mark_list.append(int(line.strip()))

def get_average(values):
    total = 0
    for i in values:
        total += i
    avg = total / len(values)
    return avg

print(get_average(mark_list))