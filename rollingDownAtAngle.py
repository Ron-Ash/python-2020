import math

def Starter():
    AngleOfElevation = float(input("Enter angle of elevation"))
    OffAxisElevation = 90-AngleOfElevation
    YAxisAcceleration = 9.8*(1-math.sin(math.radians(OffAxisElevation)))
    XAxisAcceleration = 9.8*math.cos(math.radians(OffAxisElevation))
    FinalAcceleration = math.sqrt(math.pow(XAxisAcceleration, 2) + math.pow(YAxisAcceleration, 2))
    return(FinalAcceleration, AngleOfElevation)

print(Starter())
