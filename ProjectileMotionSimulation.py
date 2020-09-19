import math
import tkinter
import turtle
import os
x = True
Gravitation = 9.80665


def TurtleSetUp(Xmotion, Ron, Gaya):
    Ron.speed(1000000)
    Gaya.speed(1000000)
    Parameter = 50
    turtle.setworldcoordinates(0, 0, Parameter*Xmotion, Parameter*Xmotion)
    Ron.color("white")
    Gaya.color("white")
    Ron.left(90)
    Ron.forward(Parameter*Xmotion/2)
    Ron.right(90)
    Gaya.left(90)
    Gaya.forward(Parameter*Xmotion/2)
    Gaya.right(90)
    

def ProjectileMotionAnimation(InitialAngle, InitialVelocity, Xmotion, Ymotion, Gravitation, x):
    

    Ron = turtle.Turtle()
    Gaya = turtle.Turtle()
    TurtleSetUp(Xmotion, Ron, Gaya)

    Gaya.color("black")
    Gaya.left(InitialAngle) 
    Gaya.forward(InitialVelocity)
    Gaya.right(InitialAngle)

    while x == True:
        Ron.color("red")
        Ron.forward(Xmotion)
        Ron.left(90)
        Ron.color("blue")
        Ron.forward(Ymotion)
        Ron.right(90)
        Ymotion -= Gravitation
        InitialVelocity = math.sqrt(math.pow(Xmotion, 2)+math.pow(Ymotion, 2))
        InitialAngle = math.degrees(math.asin(Ymotion/InitialVelocity))
        Gaya.left(InitialAngle)
        Gaya.forward(InitialVelocity)
        Gaya.right(InitialAngle)

        
def Parameter():

    InitialOrNah = input("CALCULATE FROM INITIAL VELOCITY OR NOT? \n(type Y or N)\n")
    if InitialOrNah.upper() == "Y":
        InitialVelocity = float(input("WHAT IS THE VELOCITY OF YOUR OBJECT? (m/s)\n"))
        InitialAngle = float(input("WHAT IS ITS STARTING ANGLE IN DEGREES? \n(from the X-axis anti-clockwise)\n"))
        if InitialAngle > 90:
            input("This angle cannot be calculated, try again")
            Parameter()
        Xmotion = InitialVelocity*math.cos(math.radians(InitialAngle))
        Ymotion = InitialVelocity*math.sin(math.radians(InitialAngle))
    elif InitialOrNah.upper() == "N":
        FlightTime = float(input("HOW LONG WAS THE PROJECTILE IN THE AIR?(s)\n"))
        DistanceFromStart = float(input("HOW FAR FROM THE ORIGIN DID THE PROJECTILE LAND?(m)\n"))
        Xmotion = DistanceFromStart/FlightTime
        Ymotion = (Gravitation*FlightTime)/2
        InitialAngle = math.degrees(math.atan(Ymotion/Xmotion))
        InitialVelocity = math.sqrt(math.pow(Xmotion, 2)+math.pow(Ymotion, 2))
    else:
        input("In order to calculate, one of the options must be chosen, try again")
        Parameter()
    
    
    TimeTakenToMaxHieght = Ymotion/Gravitation
    XDistanceTravelledToLandOnGround = (2*Ymotion*Xmotion)/Gravitation
    YDistanceTravelledToMaxHieght = (Ymotion**2)/(2*Gravitation)
    XDistanceTravelledToMaxHeight = (Ymotion*Xmotion)/Gravitation
    Amplitude = (0-YDistanceTravelledToMaxHieght)/(XDistanceTravelledToMaxHeight**2)

    print("__________")
    print(f"The projectile has an initial velocity of {InitialVelocity}m/s at an agle of {InitialAngle} degrees from the x-axis")
    print("-----")
    print(f"MaxHieght is at {XDistanceTravelledToMaxHeight}m, {YDistanceTravelledToMaxHieght}m after {TimeTakenToMaxHieght}s from launch")
    print("-----")
    print(f"The projectile travelled {XDistanceTravelledToLandOnGround}m along the x-axis before landing to the ground after {TimeTakenToMaxHieght*2}s")
    print("-----")
    print(f"This curve can be modelled by the formula Y = {Amplitude}(X - {XDistanceTravelledToMaxHeight}) + {YDistanceTravelledToMaxHieght}, from an original {InitialAngle} degrees")
    print("__________")

    ProjectileMotionAnimation(InitialAngle, InitialVelocity, Xmotion, Ymotion, Gravitation, x)
    
os.system("clear")
Parameter()
tkinter.mainloop()