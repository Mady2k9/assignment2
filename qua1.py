#1. Write a program which will find all such numbers which are divisible by 7 but are not a
#multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
#in a comma-separated sequence on a single line.

j=[]
a=range(2000,3200)
for i in a:
    if (i%7==0)and(i%5>0):
        j.append(str(i))
        print(j,end=",")