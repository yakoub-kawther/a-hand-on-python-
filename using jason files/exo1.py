import json
filename='file.json'

name = input("what' your name")
number=input("what's your fav number") 
data={name:number}
with open(filename ,'w') as f:
    json.dump(data, f)
with open(filename)as f:
    loaded_data=json.load(f)
    print(f"hey {name} , i know your fav number , its {loaded_data[name]}!")
