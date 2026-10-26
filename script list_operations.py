Number1 = input("what is first number? ")
Number2 = input("what is second number? ")
Number3 = input("what is third number? ")
Number4 = input("what is fourth number? ")
Number5 = input("what is fifth number? ")
my_list = []
my_list.append(Number1)
my_list.append(Number2)
my_list.append(Number3)
my_list.append(Number4)
my_list.append(Number5)


print(sorted(my_list))


sortedlist = my_list[:]
sortedlist.sort()
print(sortedlist)

NewNumber = sortedlist[:]
Number6 = input("what is your extra number? ")
NewNumber.append(Number6)
print(NewNumber)

deletedlist = NewNumber[:]
del deletedlist[0]
print(deletedlist)

reversedlist = deletedlist[:]
reversedlist.reverse()
print(reversedlist)



