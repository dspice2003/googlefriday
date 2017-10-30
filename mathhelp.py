import time

print("Hello Welcome to MathHelp.com")
time.sleep(2)

# password code

password = ""
limit = 0

username = input("Please Enter the programs username\n:")
password = input("Please Enter the programs password\n:")


while(password != "mathelp" and username != "mathelp"):
	limit = limit + 1
if(password == "mathelp" and username == "mathelp"):
	print("YOU ARE LOGED IN")
else:
	print("Access Denied")
time.sleep(2)
# password code End

# grade code

grade = input("Hello please enter your grade 2nd to 4th\n:")

time.sleep(2)
if(grade == "4th"):
	print("you have selected 4th grade")
	time.sleep(2)
	print("lets try some practice problems")
time.sleep(2)
if(grade == "3rd"):
	print("you have selected 3rd grade")
	time.sleep(2)
	print("lets try some practice problems")
time.sleep(2)
if(grade == "2nd"):
	print("you have selected 2nd grade")
	time.sleep(2)
	print("lets try some practice problems")

# grade code End

# math problems code

print("x + 25 = 50 what is x?")

x = 25
x = input("please enter the anwser\n:")

if(x == "25"):
	print("You got It!")
else:
	print("Try again")

print("lets try some more!!")
print("if x = 500 what is x + 500")
x = 1000

x = input("please enter the anwser\n:")

if(x == "1000"):
	print("You got It!")
else:
	print("Try again")

print("if x = 5000 what is 125 + x")

x = 5125
x = input("please enter the anwser\n:")

if(x == "5125"):
	print("You got It!")
else:
	print("Try again")

print("Ok you proved yourself now its going to get harder")

print("what is x + 1500 if x = 20000")

x = 20150
x = input("please enter the anwser\n:")

if(x == "20150"):
	print("You Got It!")
else:
	print("Try again")

# math problems code End
