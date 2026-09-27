#strng=''
line=''
ll=''
try:
 with open('catss.txt') as f1:
   strng=f1.readlines()
 for i in strng:
   ll += i.strip("\r\n")
 print(ll)
# with open('dogs.txt') as f2:
 #  strng2=f2.readlines()
 #for l in strng2 : 
  # line +=l.strip("\n")
 #print(line)
except FileNotFoundError:
  #print("your file is not found !")
  pass