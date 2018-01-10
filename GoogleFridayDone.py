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
time.sleep(2)
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
time.sleep(1)
print("Ok you proved yourself now its going to get harder")
time.sleep(2)
print("what is x + 1500 if x = 20000")

x = 20150
x = input("please enter the anwser\n:")

if(x == "21500"):
	print("You Got It!")
else:
	print("Try again")

# math problems code End

# Ending code
print("you have completed the program")
time.sleep(2)
print("for extra credit do you want bonus problems\n:")
time.sleep(1)
ending = input("yes or no")

if(ending == "no"):
	print("Have a good day")

if(ending == "yes"):
	print("here are more problems")

print("if x = 5,000,000,000 than what is x + 1,000,000,000,000")

x = 1005000000000 
x = input("Please enter the answer\n:")

if(x == "1,005,000,000,000"):
	print("You got it!!")
else:
	print("You tried")

print("if x = 999,999,999,999 what is 1 + x")

x = 1000000000000000
x = input("What is the answer\n:")

if(x =="1000000000000000"):
	print("you got it!!")
else:
	print("you tried")
	time.sleep(1)
print("Lets try some fractions")
	time.sleep(1)

print("what is one half in a fraction")

fraction = 1/2
fraction = ("What is the answer\n:")

if(fraction =="1/2"):
	print("You got it!!!")
else:
	print("good try")
	time.sleep(1)
print("What is one third in a fraction")

fraction = 1/3
fraction = input("what is the answer\n:")

if(fraction =="1/3"):
	print("you got it!!"
else:
	print("you tried")
	time.sleep(1)
print("OK now its going to get tricky")
	time.sleep(2)

print("what is the fraction one tenth")
	time.sleep(1)

fraction = 1/10
fraction = input("1/10  1/12")

if(fraction =="1/10"):
	print("you got it!!")
else:
	print("you tried")
	time.sleep(1)

# Ending code END

# WINNING CODE

print("OK one more and you WIN!!!")
time.sleep(2)
print("Think carefuly")
time.sleep(2)

print("lets say that there are 20 pices of pie and 8 are left. What is the fraction for 8")
time.sleep(3)

fraction = 1/8
fraction = input("1/2  1/8 or 1/20")

if(fraction =="1/8"):
	print("YOU WIN GOOD JOB YOU WON A GOLD MEDIAL!!!!!!")
else:
	print("You made it to the last question but did not win you won A SILVER MEDIAL!!!!")

# WINNING CODE END
