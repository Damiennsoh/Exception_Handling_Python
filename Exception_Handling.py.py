# Prompts user to take two integer inputs
while True:
    num1 = input("Enter first number: ")
    if num1.isdigit(): # This is a string method that checks if all characters in a string are digits.
        num1 = int(num1) # if all the characters in a string are digits, then we use the int() to convert the string digits into integers.
        break # Since it is the right input(integers), we break it from asking us the same input
    else:
        print("Please enter a valid integer.") 

while True:
    num2 = input("Enter second number: ")
    if num2.isdigit(): # We do the same thing as we did above
        num2 = int(num2)
        break
    else:
        print("Please enter a valid integer.")

while True:
    operator_choice= input("Enter operator of choice: ") # Here we choose our operator based on the calculation we want to make.
    if operator_choice in ['+', '-', '*', '/']: # If the operator is not in this list, the code will loop in order to request for a valid input.
        break
    else:
        print("Please enter a valid operator (+, -, *, /).")

# Concatenate the inputs to form a valid Python expression
"""From the equation below, the reasoning for the string function str() is that;
it converts the integer values of num1 and num2 to strings before we concatenate with the operator symbol which is a string in itself."""
equation = str(num1) + operator_choice + str(num2) # in python you can not directly concatenate strings with integers since the operator symbols are strings
 
# Evaluate the expression using eval()
while True:
    try: 
        results = eval(equation) # In this try block, the code tries to generate a result based on the equation.
        print(f"{equation} ={results}")
        with open("output.txt", "w") as f:
            f.write(f"{equation} = {results}") # This statement opens a new file called output.txt and creates an object "f" and then uses the write function write() to append the equation and the results into it. 
    
    except ZeroDivisionError: # Here an exception is raised in case a number is divided by zero, it will print the error error message out and loops from the beginning to retake inputs and an operator.
        with open("output.txt", "w") as f:
            f.write("Undefined, cannot divide by a zero") # This will print the error message into the output text file.
        print("Error! You can not divide a number by zero")   
        break
    