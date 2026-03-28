user_input = input("Enter your age: ")

try:
    age = int(user_input)  
    if age % 2 == 0:
        print("The age you entered is EVEN.")
    else:
        print("The age you entered is ODD.")
except ValueError:
    print("Value Error: Please enter a valid integer age (no decimals, letters, or symbols).")