# rainfall = [0.0, 2.5, 14.2, 6.0, 0.5, 18.7, 3.1]

# with open("rainfall.txt","w") as rain:
#     for i in rainfall:
#         rain.write(str(i) + "\n")

rainfall = []
with open("Week 7/Lab Qs/rainfall.txt", "r") as rain_file:
    for i in rain_file:
        i = i.strip()
        if i:
            rainfall.append(float(i))

# print(rainfall)

def count_wet(measurements):
    count = 0
    for w in measurements:
        if w >0:
            count += 1
    return count

# print("Number of rainy days:", count_wet(rainfall))

def find_heavy_rain(measurements,threshold):
    heavy = []
    for r in measurements:
        if r > threshold:
            heavy.append(r)
    return(heavy)

# threshold_value = int(input("Please enter the threshold:"))
# print("Number of heavy rain days:", find_heavy_rain(rainfall,threshold_value))

recent_three = rainfall[-3:]
# print(recent_three)

total_rainfall = sum(rainfall)
rainy_days = count_wet(rainfall)
over_10 = find_heavy_rain(rainfall,10)

# with open("Week 7/Lab Qs/rainfall_report.txt", "w") as report:
#     report.write("James' Rainfall Report\n")
#     report.write("=========================\n")
#     report.write(f"Total rainfall (in mm):{total_rainfall}\n")
#     report.write(f"Number of rainy days:{rainy_days}\n")
#     report.write(f"Days over 10 mm:{over_10}\n")
#     report.write(f"Rain over the last 3 days:{recent_three}\n")

# threshold_value = float(input("Please enter the threshold:"))
# while threshold_value < 0:
#     print("The threshold has to be bigger than 0")
#     threshold_value = float(input("Please enter the threshold:"))