def show(messages):
  for message in messages:
    print(message)


def send(messages):
  sent=[]
  while messages:
    message=messages.pop()
    sent.append(message)

  return sent



texts=['hello , how are you',
       'goo morning darling',
       'nice to see you guys bye!']    

show(texts)
print()
new=send(texts[:])
print()
show(new)
print()
show(texts)