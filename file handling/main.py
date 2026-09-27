from functions import *
from file_handlig import *
print("hello darling ")
gender=input("tell me whats your gender?(g/b)")
gender= genderr(gender)
words=read()
writte(words)
print(f"give me the synonyme of the word {words[0]} : ")
inp=input("....")
answ=cheking(inp , words)
l=score(answ,gender)
print(l)



