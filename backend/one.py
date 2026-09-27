# print("hi")
#f string its new methode 

first_name = "kawther"

print(f"heloo {first_name} how are you ?")

for_sal = False

if for_sal:
    print("this item is for sale")
else:
  print("it's not")

# type => to know the type of variable 

print(type(first_name))

# converting types
gpa = 305
gpa = float(gpa)
print(type(gpa))

# input accepting data

       #name = input("waht is your name ?")

# calc the area 
        #length = int(input(" length ?"))
        #width = int (input(" width ?"))

        #area = length * width
        #print(area)

# logical perators and or not  

# simple usage of if statment

user_rol = "admin"
access_level = "full" if user_rol == "admin" else "limited" 

print(access_level)

# len(name) => know the lenghth of sttring without spaces

# find() => to finde a string and return its index or -1 if not found

# rfind() => find a string starting with end 

# capitleze()
# upper() / lawer() 
# title() => capilize the first letter of each word in the string
# isdigit() => check if the string is number
# replace() => most used

phone_num ="10 12-13-14-15"
phone_num = phone_num.replace(" " ,"").replace("-","")
print(phone_num)

# displaying some values

price1 = 3.1457896
price2= -9877.12345688
price3 = 12.42

print(f"price1 = {price1:+.3f}")
print(f"price2 = {price2:.3f}")
print(f"price3 = {price3:.3f}")
