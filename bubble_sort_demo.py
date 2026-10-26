mylist = [64,24,12,22,11]
sorting = True

while sorting == True:
    sorting = False
    for i in range(len(mylist)):

        if i + 1 == len(mylist):
            continue
        else:
            if mylist[i]>mylist[i+1]:
                mylist[i], mylist[i+1] = mylist[i+1], mylist[i]
                sorting = True

