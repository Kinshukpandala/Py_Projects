#Design a simple calculator with basic arithmetic operations. Prompt the user to input two numbers and an operation choice. Perform the calculation and display the result.

#function to add two numbers
def add(a, b):
    return a + b

#function to subtract two numbers
def sub(a, b):
    return a - b

#function to multiply two numbers 
def multi(a, b):
    return a * b

#function to divide two numbers 
def div(a, b):
    if b!= 0: #The div function now checks if b is zero and returns an error message if true.
        return a / b
    else:
        print("Error! Division by zero.") 
 
while True:        #The entire program is enclosed in a while True loop to allow for repeated calculations.

#Take Inputs from the user 
    a = float(input("Enter the First Number: "))
    b = float(input("Enter the Second Number: "))

    print("Arithmetic Operation are: -\n" \
        "1. Addition\n" \
        "2. Subtraction\n" \
        "3. Multiplication\n" \
        "4. Division\n")
# \n is used to insert newline characters

    s= int(input("Select any one operation 1 ~ 4:")) # (1 ~ 4) denotes from 1 to 4 
    
    #Loop condition:
    if s == 1:
        print(a, "+", b, "=", add(a, b))

    elif s == 2:
        print(a, "-", b, "=", sub(a, b))

    elif s == 3:
        print(a, "*", b, "=", multi(a, b))

    elif s == 4:
        print(a, "/", b, "=", div(a,b))

    else:
        print("Invalid Input")

# Asking user if they want to perform another calculation
    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower() 
    # By combining both methods, helps avoid errors due to unexpected variations in user input before it is compared with the expected string 'yes'
    #.strip() removes any leading and trailing whitespace characters from the input string
    #.lower() converts all characters in the string to lowercase.
   
    if again != 'yes':
        print("Exiting the Program")
        break #breaks ends the while loop from repeated calculations
        