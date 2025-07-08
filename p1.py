#ARGUMENTS OR PARAMETERS TO USE:
name = input("What's your name? ")
print("hello,", end="")# no new line!
print(name)
print("hello","my","cuties",sep="!")# hello!my!cuties!, it adds conector bw words


#ESCAPED SEQUENCES
print("hello,", end="\n")#new line
print(name)
print("hello,", end="\t")#leaves space of a tab
print(name)


# F STRING
#when you wanna insert a variable int a string without messsing with "," or "+"...use this
print(f"hello, {name}")  # watchout for the f before the string!

name=input("whats your name bro?")

name = name.strip()  # remove whitespaces from str
name = name.capitalize()  # capitalize first word of the input
name = name.title()  # capitalise every 1st letter of all the words in input
print(f"hello, {name}")


#compressing all of this in one line
name = input("What is your name bro?\n").strip().title()
print(f"Hello, {name}")


# SPLITIING STRING
#   split user's name into first and last name
first_name, last_name = name.split(" ")
print(f"Hello, {first_name}")


#FUNCTION
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x / y)#round off to closest integer
print(z)


x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x / y, 2)#round off the answer to 2 decimal places
print(z)

#standard US way of writing numbers
x=1000
y=2000
z=x+y

print(f"{z}")#1000
print(f"{z:,}")#1,000


#DEFINE YOUR OWN FUNCTIONS
#(without parameters):
def hello():
    print("hi there")

name = input("What's your name? ").title()
hello()
print(name)

#(with parameters):
def hello(to):
    print("hi there,", to)
name = input("What's your name? ")
hello(name)#we dont need to write the print value here


def hello(to="world"):
    print("hiiii,", to)
name = input("What's your name?")
hello()
hello(name)
#use with parameters cuz its easier and efficient it helps a lot with long codes
# #also u can use a lot of vvarriables again and again
