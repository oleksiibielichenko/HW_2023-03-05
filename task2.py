
month_of_year = ['January', 'February', 'March', 'April', 'May', 'June',
                 'July', 'August', 'September', 'Oktober', 'November', 'December']

number = int(input("Enter Month number: "))

if number > 0 and number < 13:
    print(month_of_year[number - 1]),
else:
    print("Invalid Month number!")
