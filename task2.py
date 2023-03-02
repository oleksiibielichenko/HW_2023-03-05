
month_of_year = ['', 'Tuesday', 'Wednesday',
                 'Thursday', 'Friday', 'Saturday', 'Sunday']

number = int(input("Enter year month number: "))

if number > 0 and number < 8:
    print(month_of_year[number - 1]),
else:
    print("Invalid data!")
