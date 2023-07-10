'''
print("hello world")
print("my name is khaled")
# This is a comment
# these are used to explain our code

print (3+4)
print (5 * 3)
print ("6 - 2 =", 6 - 2)
print ("3 + 4 =", 3 + 4)
 # order of operations
print ((7 + 2)* 9)
print (3**2)# 3**2 = 3^2

# python can do more complex math
print("13/2 = ", 13/2)
print (13//2) # floor division
print (" 29 % 2 = ", 29 % 2)
x = 1.23425614 # round to dp
print (round(x, 2))
print (round(x, 5))
print (4//2)
x = 1
y = 4
length = 6.3
height = 12

print (height)
print (length)

# naming variables:
x1 = 3
x = 3
X = 5
_x = 4
# variable must start with small / large letter or underscore.
# must only contain letters, numbers, _

# etiquette for naming variables
# start name with small letter
# multi rod name use camel-case
# khaleddurzi x
# khaled_durzi x
# KhaledDurzi (yes)

_x=3
print (_x)


This is a comment block
we use it to comment long blocks of code



# variable typpes
x = 5 # int
y = 1.5 # float (decimal)
X = "kd" # str (string)

# strings expanded
name = "khaled"
surname = "durzi"
print (name)
num = "2"
num2 = "5"
print (num + num2)
num = int(num) # convert "2" to 2
num2 = int(num2)
print (num + num2)
print (type(num))




fl = "5.2345"
print (type(fl))
fl = float(fl)
print (type(fl))
x = 2

x = float(x)
print(x)

print (type(x))


# addition of strings
name = "khaled"
surname = "durzi"
sentence = name + " " + surname
print(sentence)
#sentence = "hi, my name is " + name + "my age is" + 17 + "."
sentence = "hi, my nsme is " + name + ", my age is " + str(17) + "."

print(sentence)

# user input
name = "khaled"
name = input("what is your name?")
age = input(" how old are you?")
sentence = "hi, my nsme is " + name + ", my age is " + str(17) + "."
print(sentence)


# avg of 3 numbers
def average(num1, num2, num3):
    add = num1 + num2 + num3
    avg = add / 3
    return avg
print(average(1, 2, 3))

# find avg of friends age
def friends():
    friend1 = input("what is your age?")
    friend2 = input("what is your age?")
    friend3 = input("what is your age?")
    add = int(friend1) + int(friend2) + int(friend3)
    avg = add / 3
    avg = round(avg, 3)
    sentence = "the average age is " + str(avg)
    return sentence
print(friends())

def weight():
    weight1 = input("What is your weight on earth? ")
    weight2 = float(weight1) * 0.38
    weight2 = round(weight2 , 2)
    return " If you weigh " + str(weight1) + " kilograms on earth, you would weight " + str(weight2) + " kilograms on mars"
print(weight())


def CoffeCup():
    Diameter = input("What is the diameter of the cup?")
    Radius = int(Diameter) / 2
    Height = input("What is the height of the cup?")
    Volume = int(Radius)**2 * int(Height) * 3.14
    VolumeR= round(Volume, 2)
    Sentence = "Since the height of the cup is " + str(Height) + " and the diameter is" + str(Diameter) + " you can fit" + str(VolumeR)
    return Sentence
print(CoffeCup())

def foodDelivery():

    tax_percentage = int(input("What is the tax percentage?"))/100
    distance_cost = float(input("How much did the driver travel?")) + 5
    food_cost = ((distance_cost)*1.2*tax_percentage)
    return "The food will cost:" + str(food_cost)
print(foodDelivery())


#conditionals
# if (condition):
# do something
# print(...)
# do multiple thingd

def grades(grade):
    if(grade > 90):
        print("Congrats! you got an A.")
grades(95) #prints the above
grades(60) #does nothing

def gradesComplex(grade):
    if (grade > 90):
         print("Congrats! you got an A.")
    else:
       print("You did not get an A")
gradesComplex(95)


def finalGrade(grade):
    if (grade > 90):
           print("You got an A")
    elif(grade > 80):
           print("You got a B")
    elif(grade > 70):
           print ("You got a C")
finalGrade(75)

# True / False in python
95 > 90 ==> True
90 > 95 ==> False
if(True):
    # do something
if(False):
    # do something
0==> False
1, 2, 3, ... ==> True
if(1): # do something
if(0) : # this will not execute


# combining conditions
80 < x < 90
x > 80 and x < 90


if(x > 80 and x < 90):
    print("Hello")

if(x > 80 or x < 50):
    print("Bye")

def money():
    Money = int(input("How much money do u have?"))
    Money1 = int(Money) // 10
    Money2 = (Money - int(Money1) * 10) // 5
    Money3 = (Money -int (Money2)*5 - int(Money1)*10) // 2
    Money4 = (Money -int(Money3)*2 - int(Money2)*5 -int(Money1)*10) // 1
    print(" you will have " + str(Money1) + " 10 coins " + str(Money2) + " 5 coins " + str(Money3) + " 2 coins " + str(Money4) + " 1 coins")

    
money()


# Loops

# print numbers 1 - 10
print(1)
print(2)
.
.
.
print(10)

# While loops
1 = 0
while i < 10:
    print(i)
    i = i + 1


def loop():
    i = 0
    while i < 10:
        print(i)
        i = i + 1
    print("done")
loop()
def cond():
    i = 0
    if i < 10:
     print(i)
     i = i + 1
    print("done")

cond()


# name == "khaled" True
# name != ""khaled" True

# check for correct password
def passcheck(correctpass):
    password = input("What is your password")
    tries = 0
    while password != correctpass and tries < 3:
        tries = tries + 1
        password = input("Try again.")
    if tries >= 3:
        print("LOCKED OUT OF APP!")
    else:
        print(" Welcome to the app")
    
passcheck("RFS")



# avg of n numbers
def avg():
    num = input("What is ur first number? ")
    add = 0
    count = 0
    while num != "stop":
        add = add + int(num)
        count = count + 1
        num = input(" Next number: ")
    avg = add / count
    print("Your average is " + str(avg))
avg()
             

# print up to a known number
def numberPrinter(n):
    i = 0
    while i < n:
        print(i + 1)
        i = i + 1
    
numberPrinter(12)


# for loop
def forNumberPrinter(n):
    for i in range(n):
        print(i)
forNumberPrinter(10)

# range()
# always stop at 'stop -1'
# range(stop) -> stop after 'n' times
# range(start, stop) -. run stop - start times
# range(start, stop, step)
# default start = 0
# default step = 1
 
def forLoops():
    print("range(5)")
    for i in range(5):
        print(i)
    print("range(5, 10)")
    for i in range(5, 10):
        print(i)

    print("range(0, 10, 2)")
    for i in range (0, 10, 2):
        print(i)

    print("range(10, 0, -1)")
    for i in range(10, 0, -1):
        print(i)


forLoops()


# small trick for writing i = 1 + i
# i = i + 1
# i += 1
# i = i - 1
# i -= 1
# i = i * 5
# i *= 5





def enough_sleep(class_taken, down_time, school_clubs, test_next_day):
    class_taken = float(class_taken * 2.5)
    down_time = int(down_time)
    school_clubs = float(school_clubs * 0.5)
    totalHours = school_clubs + down_time + class_taken
    if test_next_day == True:
        totalHours = 24 - (totalHours + 5)
    if totalHours < 6:
        print("I'm tired")
        
    elif totalHours > 6 and totalHours < 8:
        print("That's alright")
    else:
        print("Thank goodness...")
enough_sleep(6, 4, 3, 1)


def birthday_party(num_attendees, avg_age):
    if num_attendees < 15:
        print("The venue is home")
    elif num_attendees < 30 and num_attendees > 15:
        print("The venue is arcade")

    else:
        print("The venue is Amusement park")
        if avg_age < 14:
            print("Kid rides")
        else:
            print("Regular rides")
birthday_party(33, 12)
    

            
def highest_score(n):
    i = 0
    score = 0
    finalScore = 0
    if type(n) == int:
        while n > i:
            score = float(input("What is your final socre? "))
            if score > finalScore:
                finalScore = score
            i = i + 1
    
    print(float(finalScore))
    if type(n) == float:
        print(" That's not valid")

highest_score(1.5)
    

# print every individual character in s
def strLoops(s):
    for character in s:
        print(character)
strLoops("hello")

# we can use any variable name instead of character
# usually, we use characeter, char, c
# letter, l
# we can use f, i, var

# Function to find length of a string

def length(s):
    l = 0 # counting length
    for letter in s:
        l = l + 1
    return l

print(length("khaled"))

# buil-in, just like round(), print()
# print(len("hello"))

# count number of vowels in a string

def vowel(s):
    l = 0
    for letter in s:
        if letter in "AaEeIiOoUu":
            l = l + 1
            print(letter)
    return l
print(vowel("khaled"))


# function returns True if s is digit
# otherwise it returns false
# 2302332409 -> True
# 125612516g9 -> False
def isDigit(s):
    result = True
    for char in s:
        if char not in "0123456789":
            result = False
            break
    if s == "":
        result = False
    return result
print(isDigit(""))


# break, continue, pass
# break: stop the loop and move to code right after loop
# countinue: skip to the iteration
# eg: if i =5, go to i = 6
# pass: literally does nothing

# function to test these words out
def example():
    word = "go team"
    for letter in word:
        if letter in "ae":
            break
        if letter in "gt":
            continue
        if letter in " ":
            pass
        print(letter)
    print("Done")
        
example()


# copying strings
def stropy(s):
    t = ""
    for c in s:
        t+= c
    return t
print(stropy("hello"))

# s = " Ramallah friends school"
# out = "RamallahFriendsSchool"
def despace(s):
    t = ""
    for c in s:
        if c not in " ":
            t+=c
    return t
print(despace("ramallah friends school"))

# function to reverse a string
# hello --> olleh
def reverse(s):
    t = ""
    for c in s:
        t = c + t
    return t
print(reverse("hello"))

# function to mirror a string
# cat --> cattac
# faris --> farissiraf
def mirror(s):
    s = reverse(s) # code reuse
    t = ""
    for char in s:
        t = char + t + char
    return t
print(mirror("khaled"))

# string library #
import string
# module for built in strings below
def builtInStrings():
    print("letters: " + string.ascii_letters)
    print("Digits: " + string.digits)
    print("Lowercase: " + string.ascii_lowercase)
    print("punctuation: " + string.punctuation)
    print("Whitespace: " + string.whitespace)
builtInStrings()  

# this is all for the sake of readability


# advanced string methods
# string indexing
s = "hello"
print(s[0])
print(s[1])
print(len(s))

# the indec we want goes in the [square] brackets
# the result of this is one single character
# always end count at len(s) - 1

def index(s):
    print("First index: ")
    print(s[0])

    print("Second index: ")
    print(s[1])

    print("last index: ")
    print(s[len(s) - 1])
    print(s[-1])

    print("Second to last index: ")
    print(s[-2]) # dont usually use this index
s = "hello"
print(s[-5])


def loop2(s):
    for i in range(len(s)):
        print(s[i], i)
loop2("hello")

# function that returns a string with every other letter
# ramallah --> rmla
def everyother(s):
    t = ""
    for i in range(0, len(s), 2):
        t = t + s[i]
    return t
print(everyother("ramallah"))


# slicing
# s = "Ramallah"
# t = "allah"
# t = s[3:8]
# generally, [start: stop + 1: step]
# default values:
# start = 0
# end = len(string) - 1
# step = 1

def slicing():
    st = "yahyalooti"

    print(st[2:5])
    print(st[5:9])
    
    # rewrite everyother() using slicing
    print(st[0:len(st):2])

    # rewrite revers()
    print(st[::-1])



slicing()
         

def moreStrMethod(s):
    print(s.isdigit())
    print(s.isupper())
    print(s.islower())
moreStrMethod("469696969696969659696969669")

def evenMoreMethod(s):
    print(s.lower())
    print(s.upper())
evenMoreMethod('shsheuheuhseuhes')

def moreMethod(s):
    # remove all whitespace before and after string
    # s = " iwedh ikshajh "
    # returen "iwedh ikshajh"
    print(s.strip())
    print(s.strip(","))

    # find first instance of input
    # if the string doesn't have the input, -1
    print(s.find("h"))
    
def secondFind(character, string):
    firstInstance = string.find(character)
    slice = string[firstInstance + 1:]
    secondInstance = slice.find(character)
    return firstInstance + secondInstance + 1
print(secondFind("e", "elephant"))
    # elephant
    # first instance of e =0

def lists1():
    myList1 = ["red", "blue", "green"]
    myList2 = [1, 2, 3]
    myList3 = [1, "red", True]

    print(myList3)
    print(type(myList3))
    print(myList3[1]) # print the second component
    print(type(myList3[1]))
    # find length of a string
    
    print(len(myList3))
lists1()

def lists2():
    mylist = ["apples", 2, "oranges"]
    print(mylist)

    mylist[1] = "bananas"
    print(mylist)

    mylist2 = [1,2,3]
    mylist2 = mylist2 + ["Hello"]
    print(mylist2)

    mylist2.append(55)
    print(mylist2)
lists2()


# the keys in a dict can be a string or any dat
# but keys must be unique
# dict:(5: "hi", 4:"hello")

def dict1():
    # dict of keys: leyyers, values:nnumbers
    myDict = {"a": 1, "b": 2, "c": 3}
    print (type(myDict))
    print(len(myDict)) # we have 3 pairs

    print(myDict["b"])

dict1()


# function to count number of vowels
def countVowels(string):
    count = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for c in string:
        if c =="a":
            count ["a"] = count["a"] + 1
        elif c == "e":
            count ["e"] = count["e"] + 1
        elif c == "e":
            count ["i"] = count["i"] + 1
        elif c == "i":
            count ["o"] = count["o"] + 1
        elif c == "u":
            count["u"] = count["u"] + 1
    print(count)

countVowels(string)
'''

             







