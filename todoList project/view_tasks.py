import json
def view():
  """view the latest tasks"""
  file_name='my_data.jsonl'
  data=None
  with open(file_name ,'r')as f:
   for line in f:
    if line.strip():
     #print("DEBUG line:", line)
     data=json.loads(line)
  
  
  if data:
   date = list(data.keys())[0]
   print(f"the last todo list that you made in {date} :")  
   for tasks in data.values():   #get values instead of "items" key 
    for task in tasks:
       print(task)

  #else:
        #print("No 'items' key found")
  