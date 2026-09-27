from file_handlig import *
#x=1
#gender='p'

words=read()
word= writte(words)

def cheking(synonyme,words):
  """check the word"""
  i=0
  max_tries=5
  score=1
  
  #with open("words_copy.txt","r+") as f2:
    
   # words=f2.write()
  #synonyme=synonyme.strip()
  while i < max_tries:
    
    
     if synonyme in words :
      print("✅ Correct!")
      break
     else:
      i+=1
      if i < max_tries:
       synonyme = input(f"❌ Wrong! Try again ({max_tries - i} tries left): ")
       continue
  
  
  if i == max_tries:
    print(f"❌ Out of tries! The correct word was: {words[0]}")
    score += 1

  return score

def genderr(gender):
  """cheking gender"""
  if(gender=='g'):
    k='girl'
  elif(gender=='b') :
    k='boy'
  else:
    k="we don''t have this type of genders"
  return k 

def score(x,gender):
  """cheking score"""
  s=100/x
  if s>=70:
    print(f"great job baby {gender} <3 , your score is {s}")
  elif s>=50:
    print(f"you're in the right path baby {gender} (: , youre score is {s}")
  else:
    print(f"you have to work harder baby {gender} ): , youre score is {s}")

  
