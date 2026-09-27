uncompletedSandwitches=['tuna' , 'chiken' , 'meet' ,'pastrami' , 'vigitibles','pastrami' , 'fish' , 'tuna2' , 'tuna3','pastrami']

completedSandwiches=[]
print('the pastrami runs out !! \n')

while uncompletedSandwitches :
   
   sandwitch=uncompletedSandwitches.pop(0)
   if sandwitch !='pastrami':
    print(f"for {sandwitch} is comleted !")
    completedSandwiches.append(sandwitch)
   else:
     continue
   

print()
for sandwitch in completedSandwiches:
   print(sandwitch)