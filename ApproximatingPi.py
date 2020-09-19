import math
import decimal
import fractions

decimal.getcontext().prec = 1000
def ApproximatingPiThroughCircle():
    Num = decimal.Decimal(input("How accurate do you want to approximate pi?"))
    Length = decimal.Decimal(1/Num)
    Angle = decimal.Decimal(math.degrees(math.acos(((Length**2)-2)/-2)))
    NumofTriangle = 360/Angle
    Pi = Length/2*NumofTriangle

    print(Pi)

def ApproximatingPiThroughInfiniteSeries():
    PiInfinite = 0
    Numerator = 1
    Num = int(input("How accurate do you want to approximate pi?"))
    for i in range(Num):
        FractionOfPi = fractions.Fraction(1, Numerator)
        PiInfinite += FractionOfPi
        Numerator += 2
        FractionOfPi = fractions.Fraction(1, Numerator)
        PiInfinite -= FractionOfPi
        Numerator += 2
        
    PiInfinite = PiInfinite*4
    print(float(PiInfinite))

def Option():
    Answer = input("do you want to approximate Pi using area or infininte series\n(Type Area or Infinite)")
    if Answer.upper() == "AREA":
        ApproximatingPiThroughCircle()
    elif Answer.upper() == "INFINITE":
        ApproximatingPiThroughInfiniteSeries()
    else:
        input("RETRY")
        Option()

Option()
