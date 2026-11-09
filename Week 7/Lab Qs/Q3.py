num = int(input("Enter a number:"))
total = 0
count = 0
while num != 0:
    total += 1
    count += num
    num = int(input("Enter a number:"))
    
print("Program finished \n","Total count:",total, "\n Sum of all numbers:", count)