
days_of_week = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']

number = int(input("Enter week day number: "))

if number > 0 and number < 8:
    print(days_of_week[number - 1]),
else:
    print("Invalid data!")
