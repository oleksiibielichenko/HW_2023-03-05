
days_of_week = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']

number = int(input("Enter Day number: "))

if number > 0 and number < 8:
    print(days_of_week[number - 1]),
else:
    print("Invalid Day number!")
