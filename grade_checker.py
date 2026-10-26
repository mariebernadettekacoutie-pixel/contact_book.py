#Input a numeric grade from (0-100)
while True:
    grade = int(input("what is your number from (0-100)?"))

    if grade < 0 or grade > 100:
        print("Error: Please enter a valid grade between 0 and 100.")
        continue
    else: 
        if grade >= 90:
            letter_grade = "A"
        elif grade >= 80:
            letter_grade = "B"
        elif grade >= 70:
            letter_grade = "C"
        elif grade >= 60:
            letter_grade = "D"
        else:
            letter_grade = "F"
        print(f"Your grade is: {letter_grade}")
        message = "Congratulations, you passed the test!" if letter_grade in ("A","B","C") else "try again"
        print(message)

      
