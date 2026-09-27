import time
import json
def add_task():
  """to add a task"""
  tasks=[]
  print(" enter your tasts for today")
  while True:
    t=input(" ")
    tasks.append(t)
    yes_no=input("do you wann add one more(y/n)")
    yes_no=yes_no.upper()
    if yes_no=='Y':
      continue
    else:
      break
  file_name='my_data.jsonl'
  tm= time.localtime()
  tmconc= str(tm.tm_mday )+"/"+ str(tm.tm_mon) +"/"+ str(tm.tm_year)
  data= {tmconc:tasks}
  
  with open (file_name , 'a') as f :
    f.write(json.dumps(data) + "\n")

  
  

      
