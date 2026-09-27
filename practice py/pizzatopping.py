prompt='enter your topping'
prompt +='do tou wanna add more?'
message=""

while True:
  message=input(prompt)
  if message =='no':
   break
  else:
   print(message)
