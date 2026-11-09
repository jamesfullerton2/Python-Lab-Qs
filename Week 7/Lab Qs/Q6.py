loan_days = [3, 18, 7, 25, 12, 31]
def is_overdue(days):
    return days > 14

for i in loan_days:
    print(f"{i} days - overdue: {is_overdue(i)}")

def get_overdue_books(days_list):
    overdue = []
    for b in days_list:
        if is_overdue(b):
            overdue.append(b)
    return overdue

print(get_overdue_books(loan_days))

middle_four = loan_days[1:5]
print(middle_four)