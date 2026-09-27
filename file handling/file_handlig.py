
from random import choice
def read():
 with open("words.txt","r+") as f :
 #f2 = open("words_copy.txt","w+")
    lines = f.readlines()
 word=choice( lines)
  #word= lines[index]
 l=word.strip()
 return l.split()
 
def writte(l):
 with open("words_copy.txt","w+") as f2:
  f2.write(" ".join(l))
  return l
#f.close()
#f2.close()
"""
from random import randint

# Read the file
with open("words.txt", "r") as f:
    lines = f.readlines()

if not lines:
    print("The file is empty!")
else:
    # Pick a random line
    index = randint(0, len(lines) - 1)
    word = lines[index].strip()  # Remove newline

    # Split into words
    words_list = word.split()

    # Write to the new file
    with open("words_copy.txt", "w") as f2:
        f2.write(" ".join(words_list)) 

"""     
