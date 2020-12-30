from graphics import *
from time import sleep

def main():
    size, colour1, colour2, colour3 = getInputs()
    drawGrid(size, colour1, colour2, colour3)

def getInputs():
    while True:
        size = input("enter size: ")
        if size == "5" or size == "7":
            break
        print("invalid input, enter again")
    colours = "red green blue magenta orange cyan grey white"
    splitColours = colours.split() #split into list of strings
    while True:
        colourNum = 1
        colour1 = validColour(splitColours, colourNum)
        colourNum += 1
        colour2 = validColour(splitColours, colourNum)
        colourNum += 1
        colour3 = validColour(splitColours, colourNum)
        if colour1 == colour2 == colour3:
            print("invalid, there must be at least 1 different colour")
        else:
            break
    return size, colour1, colour2, colour3

def validColour(splitColours, colourNum):
    notValid = True
    while notValid:
        inputColour = input("enter colour {0}: ".format(colourNum))
        for eachColour in splitColours:
            if inputColour == eachColour:
                notValid = False
                break
        if notValid == True:
            print("invalid colour, enter again")
    return inputColour

def drawGrid(size, colour1, colour2, colour3):
    intSize = int(size)
    win = GraphWin("window", intSize*100, intSize*100)
    newSize = int((intSize+1)/2) #diagonal squares
    downSquares = 2
    upSquares = intSize - 1
    x = 0
    y = (intSize*100) - 100
    for finalPatch in range(newSize):
        finalNumberPatch(win, x, y, colour2)
        if finalPatch > 0: #add patches downwards aside from 1st box
            penNumPatch(win, x-100, y+100, colour2)
            downY = y + 100
            downY2 = y + 200
            for downFinPatch in range(downSquares):
                finalNumberPatch(win, x, downY, colour3)
                downY += 100
            for downFinPatch2 in range(downSquares-1):
                penNumPatch(win, x-100, downY2, colour3)
                downY2 += 100
            downSquares += 2
        upY = y - 100 #add patches upwards aside from last top right box
        upY2 = y - 200
        for upPenPatch in range(upSquares):
            penNumPatch(win, x, upY, colour1)
            upY -= 100
        for upPenPatch2 in range(upSquares-1):
            penNumPatch(win, x+100, upY2, colour1)
            upY2 -= 100
        upSquares -= 2
        x += 200
        y -= 200
    time.sleep(5)

def finalNumberPatch(win, x, y, colour):
    topY = y - 10 #only these 2 dimensions change
    bottomX = x + 110
    for i in range(5):
        drawSquare(win, x, topY+10, bottomX-10, y+100, "white")
        drawSquare(win, x, topY+20, bottomX-20, y+100, colour)
        topY += 20
        bottomX -= 20

def penNumPatch(win, x, y, colour):
    circleY = y
    for circleRow in range(3):
        circleX = x
        for circle in range(3):
            drawCircle(win, circleX, circleY, colour)
            drawTriangle(win, circleX, circleY, 20)
            if circle < 2:
                drawSquare(win, circleX+20, circleY, circleX+40, circleY+20, colour)
            if circleRow < 2:
                drawSquare(win, circleX, circleY+20, circleX+20, circleY+40, colour)
            if circleRow < 2 and circle < 2:
                drawCircle(win, circleX+20, circleY+20, colour)
                drawTriangle(win, circleX+20, circleY+20, 0)
            circleX += 40
        circleY += 40

def drawCircle(win, x, y, colour):
    circle = Circle(Point(x+10, y+10), 10)
    circle.setFill(colour)
    circle.draw(win)

def drawSquare(win, x, y, x2, y2, colour):
    square = Rectangle(Point(x, y), Point(x2, y2))
    square.setFill(colour)
    square.draw(win)

def drawTriangle(win, x, y, directionX):
    triangle = Polygon(Point(x+directionX, y),
    Point(x+10, y+10),
    Point(x+directionX, y+20))
    triangle.setFill("white")
    triangle.setOutline("white")
    triangle.draw(win)

main()
