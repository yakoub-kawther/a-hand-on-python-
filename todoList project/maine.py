from adding import add_task
from done import completed
from view_tasks import view
#1-adding task
#2-marking task as completed
#3-view task
#4-quite
print("hello dear , what do you want to do today?")
message="""choose a number :
1-adding task
2-marking task as completed
3-view task
4-quite
"""
print(message)
while True:
 choice=input("  ")
 try:
  choice=int(choice)
  if choice not in range(4):
   print("wrong number ! , enter one between 1 and 4 ")
   continue
 except ValueError:
  print("please enter a number not a letter !")
  continue
 else :
  break
   
while True:
  if choice == 1:
   add_task()
   break
  elif choice ==2 :
   completed() 
   break
  elif choice == 3:
   view()
   break
  elif choice==4:
   break
