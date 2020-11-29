#-------------------------------------------------------------------------------
# Practical Worksheet 6: if statements and for loops
# Rupert Acuesta
# 2016499
#-------------------------------------------------------------------------------

from graphics import *
import math
import random

# For exercises 8 & 11
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

# For exercise 8
#def drawColouredEye(win, centre, radius, colour):
    #pass
    # remove the pass and add your code here





#exercise 1
def fastFoodOrderPrice():
    price = int(input("enter price: "))
    totalPrice = 1.50 + price
    if price >= 10:
        totalPrice = 0
    print("total price is ", totalPrice)

#exercise 2
def whatToDoToday():
    temp = int(input("enter temperature: "))
    if temp > 25:
        print("have a swim")
    elif temp <= 25 and temp >= 10:
        print("shop at Gunwharf")
    else:
        print("watch a film")

#exercise 3
def displaySquareRoots(start, end):
    for number in range(start, end + 1):
        root = math.sqrt(number)
        print("The square root of ", number, " is {0:0.3f}".format(root))

#exercise 4
def calculateGrade(mark):
    if mark <= 20 and mark >= 16:
        return "A"
    elif mark <= 15 and mark >= 12:
        return "B"
    elif mark <= 11 and mark >= 8:
        return "C"
    elif mark < 8 and mark >= 1:
        return "F"
    else:
        return "X"

#exercise 5
def peasInAPod():
    num = int(input("enter number: "))
    win = GraphWin("window", 100 * num, 100)
    centre = 0
    for i in range(num):
        circle = Circle(Point(centre + 50, 50), 50)
        circle.setFill("green")
        circle.draw(win)
        centre += 100

#exercise 6
def ticketPrice(distance, age):
    ticketCost = 3.00
    eachKilometre = 0.15
    totalCost = ticketCost + (distance * eachKilometre)
    if age >= 60 or age <= 15:
        discount = totalCost * 0.4
        totalCost -= discount
    return totalCost

#exercise 7
def numberedSquare(n):
    for i in range(n, 0, -1):
        for j in range(i, i+n):
            print(j, end=" ")
        print()

#exercise 8
def drawColouredEye(win, centre, radius, colour):
    outerEye = Circle(centre, radius)
    colouredEye = Circle(centre, radius-15)
    colouredEye.setFill(colour)
    innerEye = Circle(centre, radius-35)
    innerEye.setFill("black")
    outerEye.draw(win)
    colouredEye.draw(win)
    innerEye.draw(win)

def eyePicker():
    x = int(input("enter x value: "))
    y = int(input("enter y value: "))
    centrePoint = Point(x, y)
    radius = int(input("enter radius: "))
    colour = input("enter colour: ")
    if colour == "blue" or colour == "grey" or colour == "green" or colour == "brown":
       drawColouredEye(GraphWin("window", 500, 500), centrePoint, radius, colour)
    else:
        print("not valid eye colour")

#exercise 9
def drawPatchWindow():
    win = GraphWin("window", 200, 200)
    tX = 0
    tY = -10
    bX = 110
    bY = 100
    for i in range(5):
        whiteRectangle = Rectangle(Point(tX, tY+10), Point(bX-10, bY))
        whiteRectangle.setFill("white")
        whiteRectangle.setOutline("white")
        whiteRectangle.draw(win)

        redRectangle = Rectangle(Point(tX, tY+20), Point(bX-20, bY))
        redRectangle.setFill("red")
        redRectangle.setOutline("white")
        redRectangle.draw(win)

        tY += 20
        bX -= 20

#exercise 10
def drawPatch(win, x, y, colour):
    tX = x
    tY = y
    bX = x + 110
    bY = y + 110

    for i in range(5):
        whiteRectangle = Rectangle(Point(tX, tY+10), Point(bX-10, bY))
        whiteRectangle.setFill("white")
        whiteRectangle.setOutline("white")
        whiteRectangle.draw(win)

        redRectangle = Rectangle(Point(tX, tY+20), Point(bX-20, bY))
        redRectangle.setFill(colour)
        redRectangle.setOutline("white")
        redRectangle.draw(win)

        tY += 20
        bX -= 20

def drawPatchWork():
    win = GraphWin("window", 300, 200)
    x = 0
    y = -110
    colour = "blue"
    for i in range(2):
        nextX = 0
        drawPatch(win, x, y+100, colour)
        for j in range(2):
            drawPatch(win, nextX+100, y+100, colour)
            nextX += 100
        y += 100

#exercise 11
def eyesAllAround():
    win = GraphWin("window", 500, 500)
    colours = "blue grey green brown"
    splitColours = colours.split()

    eachColour = 0
    for i in range(30):
        if eachColour == 4:
            eachColour = 0
        else:
            centre = win.getMouse()
            drawColouredEye(win, centre, 30, splitColours[eachColour])
            eachColour += 1

#exercise 12
def atmosConditions():
    x = random.randint(1, 10)
    return x

def distanceBetweenPoints(p1, p2):
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    #return Pythagoras Theorem
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def archeryGame():
    win = GraphWin("window", 300, 300)
    colours = "blue red yellow"
    splitColours = colours.split()
    centre = Point(150, 150)
    
    eachColour = 0
    radius = 100
    direction = 0
    points = 0
    pointsLabel = Text(Point(150, 30), "")

    for i in range(3):
        drawCircle(win, centre, radius, splitColours[eachColour])
        eachColour += 1
        radius -= 40
        
    for j in range(5):
        shot = win.getMouse()
        if direction == 1:
            direction = 0
            shotChange= Point(shot.getX() + float(atmosConditions()), shot.getY() - float(atmosConditions()))
            shotChange.draw(win)
        else:
            shotChange = Point(shot.getX() - float(atmosConditions()), shot.getY() + float(atmosConditions()))
            shotChange.draw(win)
            direction += 1
            
        if distanceBetweenPoints(centre, shotChange) < 100 and distanceBetweenPoints(centre, shotChange) > 60:
            points += 2
        elif distanceBetweenPoints(centre, shotChange) < 60 and distanceBetweenPoints(centre, shotChange) > 20:
            points += 5
        elif distanceBetweenPoints(centre, shotChange) < 20:
            points += 10;
        
    pointsLabel.setText("your score is {0}".format(points))
    pointsLabel.draw(win)



