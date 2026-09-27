prompt1='if you want to visit a place in the world , where would you go ?'
prompt2='what is your name'
answers={}
cnt=True

while cnt:
  name=input(prompt2)
  place=input(f'{name} {prompt1}')
  answers[name]=place

  end=input('do u wanna continue(y/n)')
  if end=='y':
    continue
  else:
    cnt=False
  
for name , place in answers.items():
  print(f"{name} want to go to {place}")
