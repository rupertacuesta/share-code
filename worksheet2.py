import math

pi = math.pi

def circumferenceOfCirlce():
    r = float(input("Enter radius: "))
    print("circumference ", 2 * pi * r)

def areaOfCircle():
    r = float(input("radius of circle: "))
    print("area: ", pi * r ** 2)

def costOfPizza():
    #1.5p per cm
    diameter = float(input("Enter diameter: "))
    radius = diameter / 2
    area = pi * radius**2 
    print("the cost is: ", area * 1.5) 
    

def slopeOfLine():
    x1 = int(input("x1 = "))
    y1 = int(input("y1 = "))
    x2 = int(input("x2 = "))
    y2 = int(input("y2 = "))
    top = y2 - y1
    bottom = x2 - x1
    print("slope: ", top / bottom)

def distanceBetweenPoints():
    x1 = int(input("x1 = "))
    y1 = int(input("y1 = "))
    x2 = int(input("x2 = "))
    y2 = int(input("y2 = "))
    calculate = (x2 - x1)**2 + (y2 - y1)**2
    print("distance: ", math.sqrt(calculate))

def travelStatistics():
    speed = float(input("Average speed: "))
    dur = float(input("duration: "))
    distance = speed * dur
    #fuel efficiency of 5km/litre, for every 5km is a litre used
    fuel = distance / 5
    print("distance in km: ", distance) 
    print("fuel used in litres: ", fuel)

def sumOfSquares(): 
    number = int(input("enter value: "))
    sumOf = 0
    for i in range(1,number+1):
        sumOf = sumOf + i**2 
    print(sumOf)

def averageOfNumbers():
    #average = add all up divide by amount
    amount = int(input("How many numbers: "))
    y = 0
    for i in range(amount):
        i = i + 1
        number = int(input("Enter number: ")) 
        y = y + number
        #for loop finishes
    print("average: ", y / amount)

# HARDER
def fibonacci(): 
    nth = int(input("Enter value: "))
    number1 = 0
    number2 = 1
    for i in range(1, nth + 1):
        #store in separate variable
        x = number1 + number2
        #assign to previous value in sequence
        number2 = number1
        number1 = x
    print(number1) 
    
# fibonacci sequence
# i1 = 1
# i2 = 1
# i = i1 + i2
# i1 = i
# i2 = i1


# // whole number   
# % remainder

# coin question
# p = 35
# twentyp = p // 20
# p = p % 20
# tenp = p//10
# p = p%10