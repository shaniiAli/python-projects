def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


number_of_people = int(input("Enter the number of people in the group: "))
names = []

for i in range(number_of_people):
    name = input(f"Enter the name of person {i+1}:").strip()
    names.append(name)
    
total_bill = get_float("Enter the total bill amount: ")

share = round(total_bill/number_of_people , 2)
print("\n" + "*" * 40)
print(f"The total bill amount is: ${total_bill:.2f}")
print(f"Each person should pay: ${share}")
print("The people in the group are:")
for name in names:
    print(f"- {name}")
print("*" * 40 + "\n")