#Rupert Acuesta, 2016499

from graphics import *

#1
def personalGreeting():
    name = input("Enter name: ")
    print("Hello " + name + ", nice to see you!")


#2
def formalName():
    firstName = input("first name: ")
    lastName = input("last name: ")
    print(firstName[0].upper() + ". " + lastName)

    
#3
def kilos2pounds():
    kilos = float(input("Enter kilo amount: "))
    pounds = kilos * 2.2
    print("{0:0.2f} kilos is equal to {1:0.2f} pounds".format(kilos, pounds))


#4
def generateEmail():
    firstName = input("first name: ")
    lastName = input("last name: ")
    entryYear = (input("entry year: ")) 

    fourLetters = lastName[:4]
    firstLetter = firstName[0]
    twoDigits = entryYear[2:4]

    print(fourLetters + "." + firstLetter + "." + twoDigits + "@myport.ac.uk")


#5
def gradeTest():
    grades = "FFFFCCBBAAA"
    mark = int(input("enter mark: "))
    print("your grade is " + grades[mark])


#6
def graphicLetters():
    word = input("enter word: ")
    win = GraphWin("graphic letters", 400, 400)

    #chosen point
    for letter in word:
        point = win.getMouse()
        showLetter = Text(Point(point.getX(), point.getY()), letter)
        showLetter.draw(win)


#7
def singASong():
    word = input("enter word: ")
    lines = int(input("amount of lines: "))
    wordRepeat = int(input("words per line: "))

    for i in range(lines):
        print((word + " ") * wordRepeat)


#8
def exchangeTable():
    for euro in range(1, 21):
        pound = euro * 1.10
        print(euro, " {0:8.2f}".format(pound))

#9
def makeInitialism():
    phrase = input("enter phrase: ")
    splitPhrase = phrase.split()

    for i in splitPhrase:
        print(i[0].upper(), end="")


#10
def nameToNumber():
    alph = "abcdefghijklmnopqrstuvwxyz"
    
    name = input("enter name: ")
    nameLower = name.lower()
    total = 0
    
    for letter in nameLower:
        value = alph.find(letter) 
        total += value + 1
    print("value of your name: ", total)
   
              
#11
def fileInCaps():
    fileName = input("enter file name: ")
    openFile = open(fileName + ".txt", "r")
    for contents in openFile:
        print(contents.upper())
    openFile.close() 

    
#12
def rainfallChart():
	openFile = open("rainfall.txt", "r")
	contents = openFile.readlines()
	for line in contents:
		splitContents = line.split()
		print(splitContents[0] + " " + "*" * int(splitContents[1]))
	openFile.close()


#13    
def rainfallInInches():
	openFile = open("rainfall.txt", "r")
	newFile = open("question13.txt", "w")
	contents = openFile.readlines()
	for line in contents:
		splitContents = line.split()
		print(splitContents[0] + " " + " {0:0.2f}".format(int(splitContents[1]) / 25.4), file=newFile)
	openFile.close()
	newFile.close()


#14
def wc():
    fileName = input("enter filename: ")
    openFile = open(fileName + ".txt", "r")
    contents = openFile.read()

    #character count 
    removeSpaces = contents.replace(" ", "")
    removeLines = removeSpaces.replace("\n", "")
    characterCount = 0
    for i in removeLines:
        characterCount += 1
    print("number of characters: ", characterCount)

    #word count
    splitContents = contents.split()
    wordCount = 0
    for i in splitContents:
        wordCount = wordCount + 1
    print("number of words: ", wordCount)
    openFile.close()
    
    #line count
    openFile2 = open(fileName + ".txt", "r")
    contents2 = openFile2.readlines()
    lineCount = 0
    for i in contents2:
        lineCount += 1
    print("number of lines: ", lineCount)
    openFile2.close()





