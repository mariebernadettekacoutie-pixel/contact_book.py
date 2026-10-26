total = 0
for number in range(1,51):
    if number % 2 == 0:
        total += number
    else:
        continue
print("the sum of even numbers from 1 to 50 is", total)



total = 0
number = 1
while number < 51:
    if number % 2 == 0:
        total += number
        number += 1
    else:
        number += 1
        continue
print("the sum of even numbers from 1 to 50 is", total)
