print("if you want quite , press 'q'")
x=''
y=0
while True:
  try:
    x= input(" ")
    if x=='q':
     break
    else:
     y=int(x)
     y+=y
  except ValueError:
    pass
  
print(y)
  