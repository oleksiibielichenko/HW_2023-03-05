
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
list_of_numbers = []
list_of_numbers.append(num_1)
list_of_numbers.append(num_2)
print(list_of_numbers)
sorted_list_of_numbers = sorted(list_of_numbers)
if num_1 == num_2:
    print("Number is equal")
else:
    print(sorted_list_of_numbers)
