import math
prompt1="inter the first list"
prompt2="inter the second one"
list1=[]
list2=[]

i=0
j=0


print(prompt1)
while True:
  distance=input(" ")
  list1.append(distance)
  respoce=input("do you want to continue (y/n)")
  if respoce.lower()=='y':
       continue
  if respoce.lower()=='n':
       
       break

input(prompt2)
for _ in range(len(list1)):
    distance=input(" ")
    list2.append(distance)

list1.sort()
list2.sort()
finalList=[]
copie1=list1[:]
copie2=list2[:]

j=0
for j in range(i-1):
    num1=list1.pop()
    num2=list2.pop()
    realOne= abs(int(num1) - int(num2) )
    finalList.append(realOne)

sum = sum(finalList)


print(f"total distance is {sum}")