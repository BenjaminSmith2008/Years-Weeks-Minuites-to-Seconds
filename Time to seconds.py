print("Welcome to the time to seconds converter.")
while True:
    try:
        years = int(input("Please input the number of years: "))
        break
    except ValueError:
        print("Make sure to enter the number of years in number form.")
        print("Please try again")

while True:
    try:
        weeks = int(input("Please input the number of weeks: "))
        break
    except ValueError:
        print("Make sure to enter the number of weeks in number form.")
        print("Please try again")

while True:
    try:
        days = int(input("Please input the number of days: "))
        break
    except ValueError:
        print("Make sure to enter the number of days in number form.")
        print("Please try again")

total_days = years * 365 + weeks * 7 + days
total_seconds = total_days * 24 * 60 * 60

print(str(years) + " years, " + str(weeks) + " weeks and " + str(days) + " days is equivalent to " + str(total_seconds) + " seconds.")
