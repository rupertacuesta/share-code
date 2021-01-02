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
    validColours = "red green blue magenta orange cyan"
    splitColours = validColours.split() #split into list of strings
    while True:
        colourNum = 1
        colour1 = checkValid(splitColours, colourNum)
        colourNum += 1
        colour2 = checkValid(splitColours, colourNum)
        colourNum += 1
        colour3 = checkValid(splitColours, colourNum)
        if colour1 == colour2 == colour3: #must be 1 different colour
            print("invalid, there must be at least 1 different colour")
        else:
            break
    return int(size), colour1, colour2, colour3

def checkValid(splitColours, colourNum):
    notValid = True
    while notValid:
        inputColour = input("enter colour {0}: ".format(colourNum))
        for colour in splitColours: #loop through each colour
            if inputColour == colour:
                notValid = False
                break
        if notValid == True:
            print("invalid colour, enter again")
    return inputColour
# blue green red
def drawGrid(size, colour1, colour2, colour3):
    win = GraphWin("window", size*100, size*100)
    x = 0
    y = (size*100) - 100
    bottomSquares = 1
    topSquares = size - 1
    for diagonalSquare in range(size):
        if(diagonalSquare % 2) == 0:
            finalNumPatch(win, x, y, colour2)
        else:
            penNumPatch(win, x, y, colour2)
        if diagonalSquare > 0:
            downY = y + 100
            for bottomSide in range(bottomSquares):
                if(bottomSquares % 2) == 0:
                    finalNumPatch(win, x, downY, colour3)
                else:
                    penNumPatch(win, x, downY, colour3)
                downY += 100
            bottomSquares += 1
        if diagonalSquare < size:
            upY = y - 100
            for topSide in range(topSquares):
                penNumPatch(win, x, upY, colour1)
                upY -= 100
            topSquares -= 1
        x += 100
        y -= 100
    time.sleep(3)

def finalNumPatch(win, x, y, colour):
    topY = y - 10 #only these 2 dimensions change
    bottomX = x + 110
    for i in range(5):
        drawSquare(win, x, topY+10, bottomX-10, y+100, "white")
        drawSquare(win, x, topY+20, bottomX-20, y+100, colour)
        topY += 20
        bottomX -= 20

def penNumPatch(win, x, y, colour):
    circleY = y #circles going downwards
    for circleRow in range(3):
        circleX = x #circles going to the right
        for circle in range(3):
            drawCircle(win, circleX, circleY, colour)
            drawTriangle(win, circleX, circleY, 20)
            if circle < 2:
                drawSquare(win, circleX+20, circleY,
                circleX+40, circleY+20, colour)
            if circleRow < 2:
                drawSquare(win, circleX, circleY+20,
                circleX+20, circleY+40, colour)
            if circleRow < 2 and circle < 2:
                drawCircle(win, circleX+20, circleY+20, colour)
                drawTriangle(win, circleX+20, circleY+20, 0)
            circleX += 40
        circleY += 40

def drawCircle(win, x, y, colour):
    circle = Circle(Point(x+10, y+10), 10)
    circle.setFill(colour)
    circle.setOutline(colour)
    circle.draw(win)

def drawSquare(win, x, y, x2, y2, colour):
    square = Rectangle(Point(x, y), Point(x2, y2))
    square.setFill(colour)
    square.setOutline(colour)
    square.draw(win)

def drawTriangle(win, x, y, directionX): #directionX determines whether arrow faces left or right
    triangle = Polygon(Point(x+directionX, y),
    Point(x+10, y+10),
    Point(x+directionX, y+20))
    triangle.setFill("white")
    triangle.setOutline("white")
    triangle.draw(win)

main()
