import os
""""
print(os.getcwd())

file=open("hello.txt")
print(file)
print(os.path.abspath(__file__))
"""
print(os.path.dirname(os.path.abspath(__file__)))