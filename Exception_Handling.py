# Prompts user to take two integer inputs
while True:
    choice = input("Enter '1' to input two integers or '2' to select from a file: ")
    if choice == "1":

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
               with open("output.txt", "a") as f:
                 f.write(f"\n{equation} = {results}") # This statement opens a new file called output.txt and creates an object "f" and then uses the write function write() to write the equation and the results into it. 
                 break
            except ZeroDivisionError: # Here an exception is raised in case a number is divided by zero, it will print the error error message out and loops from the beginning to retake inputs and an operator.
               with open("output.txt", "a") as f:
                 f.write("\nUndefined, cannot divide by a zero") # This will print the error message into the output text file.
                 print("Error! You can not divide a number by zero")   
                 break
                
    elif choice == "2": # if the user decides to select from a file the code in this block will execute.
        filename = input("Enter the file's name: ")
        print("Below are the lines of expressions and their respective results")
        try:
           with open(filename, "r") as file:

            '''The for loop iterates over the file object itself, 
            which automatically reads one line at a time from the file. 
            Each line is stripped of any leading or trailing whitespace using the strip() method, 
            and the resulting expression is evaluated using the eval() function.'''
            for line in file.readlines():
                try:
                    # Remove leading and trailing whitespace from the line
                    expression = line.strip()
                    
                    #Skip empty lines
                    if not line:
                        continue
                    print(expression)
                except Exception as e:
                    print(f"An error occurred: {e}")
        except FileNotFoundError:
            print(f"Error: {filename} not found Please choose the right file and try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # if option '2' is not take print the below code
    else:
        print("Invalid choice.! Please try again")
    #break # This keyword break stops the code from looping from the beginning.

    continue_stop = input("Press 'C' to continue or 'S' to stop: ")
    if continue_stop.lower() == "s":
        break
    
    

