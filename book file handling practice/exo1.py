file = 'file_py.txt'
strng=''
with open(file) as f:
  lines=f.readlines()

for i in lines:
  strng += i.strip()

for _ in range(3):
 print(strng)
 print()


strng=strng.replace('rain' , 'snow')
print(strng)