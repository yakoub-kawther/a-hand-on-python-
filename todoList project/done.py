import json
def completed():
  """completed tasks"""
  file_name='my_data.jsonl'
  #data=None
  #i=0
  #k=0
  
  
  with open(file_name ,'r',encoding='utf-8') as f:
    for line in f :
      if line.strip():
       data =[json.loads(line)]
       realdata=[json.loads(line)]
  ans=input("wich task that you done from ?")     


  last_data=data[-1]
  date = list(last_data.keys())[0]
  tasks=last_data[date]
  #if data:
  for indx,task in enumerate(tasks):
     if task == ans:
       tasks[indx] = task + "✅"
       print(f"Marked '{ans}' as completed.")
       break
  realdata[-1]={date:tasks}    
       
  
  with open(file_name, 'w' , encoding='utf-8') as f:
        for entry in realdata:
            f.write(json.dumps(entry , ensure_ascii=False) + "\n")