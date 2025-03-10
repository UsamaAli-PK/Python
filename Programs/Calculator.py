num1 = input("Enter a number: ")
num2 = input("Enter a second number: ")

num1 = float(num1)
num2 = float(num2)

print("\nSelect an option:")
print("Addition (A)")
print("Subtraction (S)")
print("Multiplication (M)")
print("Division (D)")
print("Exit (E)")


choice = input("Enter your choice: ").upper()

if choice == "A":
    result = num1 + num2
    print(num1, " + ", num2, " = ", result)
elif choice == "S":
    result = num1 - num2
    print(num1, " - ", num2, " = ", result)
elif choice == "M":
    result = num1 * num2
    print(num1, " * ", num2, " = ", result)
elif choice == "D":
    if num2 == 0:
        print("Error! Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(num1, " / ", num2, " = ", result)
elif choice == "E":
    print("Exiting the program...")
    exit()
else:
    print("Invalid choice! Please try again.")
