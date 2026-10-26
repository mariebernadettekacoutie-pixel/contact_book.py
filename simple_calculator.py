#get user to input (2) numbers

question1 =(input("what is your first number?"))
question2 =(input("what is your second number?"))


if question1.isdigit() and question2.isdigit():
    
        print("your numbers are valid")
  
else:
        print("insert a valid number")
        

operators = input("choose an operator (+, -, *, /):")
if operators == "+":
    result = question1 + question2

elif operators == "-":
    result = question1 - question2
elif operators == "*":
    result = question1 * question2
elif operators == "/":
        print(f"the result is {result}")
        
    if question2 != 0:
        result = question1 / question2
            print(f"the result is {result}")
   
    else:
        print("the result is not a divider")

else:
    print("choose a valid operator")


