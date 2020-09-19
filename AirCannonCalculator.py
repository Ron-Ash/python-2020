import math
import turtle


def TurtleSetUp(XmotionOJVel, YmotionOJF, Ron, Allen, InitialAngle):
    Ron.speed(1000000)
    Allen.speed(1000000)
    Parameter = 550
    if InitialAngle>=45:
        turtle.setworldcoordinates(0, 0, Parameter*YmotionOJF/2, Parameter*YmotionOJF/2)
    elif InitialAngle<45:
        turtle.setworldcoordinates(0, 0, Parameter*XmotionOJF/2, Parameter*XmotionOJF/2)
    Ron.color("white")
    Allen.color("white")
    Ron.left(90)
    Allen.left(90)
    Ron.forward(Parameter*XmotionOJVel/4)
    Allen.forward(Parameter*XmotionOJVel/4)
    Ron.right(90)
    Allen.right(90)



def DrawIt(InitialAngle, XmotionOJF, YmotionOJF, XmotionLifF, YmotionLifF, XmotionDragF, YmotionDragF, g, Cd, Cl, P, m, SA, t):
    Ron = turtle.Turtle()
    Allen = turtle.Turtle()
    TurtleSetUp(XmotionOJF, YmotionOJF, Ron, Allen, InitialAngle)
    print(InitialAngle, XmotionOJF, YmotionOJF, XmotionLifF, YmotionLifF, XmotionDragF, YmotionDragF, g, Cd, Cl, P, m, SA, t)
    Allen.color("black")
    InitialF = math.sqrt(math.pow(XmotionOJF, 2)+math.pow(YmotionOJF, 2))
    InitialAngle = math.degrees(math.asin(YmotionOJF/InitialF))
    Allen.left(InitialAngle)
    Allen.forward(InitialF/m)
    Allen.right(InitialAngle)
    Drawing = False


    while Drawing == False:
        Ron.color("red")
        Ron.forward(XmotionOJF/m)
        Ron.left(90)
        Ron.color("blue")
        Ron.forward(YmotionOJF/m)
        Ron.right(90)

        XmotionDragF = -(Cd*P*((XmotionOJF/m*t)**2)/2*SA)/m
        YmotionDragF = -(Cd*P*((YmotionOJF/m*t)**2)/2*SA)/m


        XmotionLifF = -(Cl*P*((XmotionOJF/m*t)**2)/2*SA)/m
        YmotionLifF = (Cl*P*((YmotionOJF/m*t)**2)/2*SA)/m


        YmotionOJF += YmotionDragF+YmotionLifF+g

        if XmotionOJF>0:
                XmotionOJF += XmotionDragF+XmotionLifF
        elif XmotionOJF<=0:
                XmotionOJF = 0

        InitialF = math.sqrt(math.pow(XmotionOJF, 2)+math.pow(YmotionOJF, 2))
        InitialAngle = math.degrees(math.asin(YmotionOJF/InitialF))
        Allen.left(InitialAngle)
        Allen.forward(InitialF/m)
        Allen.right(InitialAngle)


        



def CannonBaby():
    Cd = 0.507
    P = 1.21
    g = -9.81
    Cl = 0.208
    print("Answer the following in SI units\n----------")
    PSI = float(input("What is the PSI bro?\t"))
    s = float(input("How long is your barrel?\t"))
    r = float(input("What is the radius of your balls?\t"))
    m = float(input("How heavy are they?\t"))
    InitialAngle = float(input("What angle are you shooting from?\t"))
    SA = math.pi*r**2
    Pa = PSI*6894.76
    Initial_F = Pa*SA
    Initial_A = Initial_F/m
    t = math.pow((2*s/Initial_A),0.5)
    VelocityOutOfBarrel = t*Initial_A
    XmotionOJF = Initial_F*math.cos(math.radians(InitialAngle))
    YmotionOJF = Initial_F*math.sin(math.radians(InitialAngle))

    DragF = (Cd*P*(VelocityOutOfBarrel**2)/2*SA)
    XmotionDragF = DragF*math.cos(math.radians(InitialAngle+180))
    YmotionDragF = DragF*math.sin(math.radians(InitialAngle+180))

    LiftF = (Cl*P*(VelocityOutOfBarrel**2)/2*SA)
    XmotionLifF = LiftF*math.cos(math.radians(InitialAngle+90))
    YmotionLifF = LiftF*math.sin(math.radians(InitialAngle+90))

    DrawIt(InitialAngle, XmotionOJF, YmotionOJF, XmotionLifF, YmotionLifF, XmotionDragF, YmotionDragF, g, Cd, Cl, P, m, SA, t)
CannonBaby()
