import math
################################ FUNCTIONS AND CLASSES ################################
# Metric Conversion Functions #
def Picometers(endingUnit):
    match endingUnit:
        case "picometers":
            convertedNum = numToConvert 
            printConversion(numToConvert, convertedNum)
        case "nanometers":
            convertedNum = numToConvert / (10**3)
            printConversion(numToConvert, convertedNum)
        case "micrometers":
            convertedNum = numToConvert / (10**6)
            printConversion(numToConvert, convertedNum)
        case "millimeters":
            convertedNum = numToConvert / (10**9)
            printConversion(numToConvert, convertedNum)
        case "centimeters":
            convertedNum = numToConvert / (10**10)
            printConversion(numToConvert, convertedNum)
        case "decimeters":
            convertedNum = numToConvert / (10**11)
            printConversion(numToConvert, convertedNum)
        case "meters":
            convertedNum = numToConvert / (10**12)
            printConversion(numToConvert, convertedNum)
        case "decameters":
            convertedNum = numToConvert / (10**13)
            printConversion(numToConvert, convertedNum)
        case "hectometers":
            convertedNum = numToConvert / (10**14)
            printConversion(numToConvert, convertedNum)
        case "kilometers":
            convertedNum = numToConvert / (10**15)
            printConversion(numToConvert, convertedNum)
        case "megameters":
            convertedNum = numToConvert / (10**18)
            printConversion(numToConvert, convertedNum)
        case "gigameters":
            convertedNum = numToConvert / (10**21)
            printConversion(numToConvert, convertedNum)
        case "terameters":
            convertedNum = numToConvert / (10**24)
            printConversion(numToConvert, convertedNum)
        case "inches":
            convertedNum = numToConvert * 0.0000000000393701
            printConversion(numToConvert, convertedNum)
        case "feet":
            convertedNum = numToConvert * 0.00000000000328084
            printConversion(numToConvert, convertedNum)
        case "yards":
            convertedNum = numToConvert * 0.00000000000109361
            printConversion(numToConvert, convertedNum)
        case "miles":
            convertedNum = numToConvert * 0.000000000000000621371
            printConversion(numToConvert, convertedNum)

def Nanometers(endingUnit):
    match endingUnit:
        case "picometers":
            convertedNum = numToConvert * (10**3)
            printConversion(numToConvert, convertedNum)
        case "nanometers":
            convertedNum = numToConvert 
            printConversion(numToConvert, convertedNum)
        case "micrometers":
            convertedNum = numToConvert / (10**3)
            printConversion(numToConvert, convertedNum)
        case "millimeters":
            convertedNum = numToConvert / (10**6)
            printConversion(numToConvert, convertedNum)
        case "centimeters":
            convertedNum = numToConvert / (10**7)
            printConversion(numToConvert, convertedNum)
        case "decimeters":
            convertedNum = numToConvert / (10**8)
            printConversion(numToConvert, convertedNum)
        case "meters":
            convertedNum = numToConvert / (10**9)
            printConversion(numToConvert, convertedNum)
        case "decameters":
            convertedNum = numToConvert / (10**10)
            printConversion(numToConvert, convertedNum)
        case "hectometers":
            convertedNum = numToConvert / (10**11)
            printConversion(numToConvert, convertedNum)
        case "kilometers":
            convertedNum = numToConvert / (10**12)
            printConversion(numToConvert, convertedNum)
        case "megameters":
            convertedNum = numToConvert / (10**15)
            printConversion(numToConvert, convertedNum)
        case "gigameters":
            convertedNum = numToConvert / (10**18)
            printConversion(numToConvert, convertedNum)
        case "terameters":
            convertedNum = numToConvert / (10**21)
            printConversion(numToConvert, convertedNum)
        case "inches":
            convertedNum = numToConvert * 0.0000000393701
            printConversion(numToConvert, convertedNum)
        case "feet":
            convertedNum = numToConvert * 0.00000000328084
            printConversion(numToConvert, convertedNum)
        case "yards":
            convertedNum = numToConvert * 0.00000000109361
            printConversion(numToConvert, convertedNum)
        case "miles":
            convertedNum = numToConvert * 0.000000000000621371
            printConversion(numToConvert, convertedNum)

def Micrometers(endingUnit):
    match endingUnit:
        case "picometers":
            convertedNum = numToConvert * (10**6)
            printConversion(numToConvert, convertedNum)
        case "nanometers":
            convertedNum = numToConvert * (10**3)
            printConversion(numToConvert, convertedNum)
        case "micrometers":
            convertedNum = numToConvert 
            printConversion(numToConvert, convertedNum)
        case "millimeters":
            convertedNum = numToConvert / (10**3)
            printConversion(numToConvert, convertedNum)
        case "centimeters":
            convertedNum = numToConvert / (10**4)
            printConversion(numToConvert, convertedNum)
        case "decimeters":
            convertedNum = numToConvert / (10**5)
            printConversion(numToConvert, convertedNum)
        case "meters":
            convertedNum = numToConvert / (10**6)
            printConversion(numToConvert, convertedNum)
        case "decameters":
            convertedNum = numToConvert / (10**7)
            printConversion(numToConvert, convertedNum)
        case "hectometers":
            convertedNum = numToConvert / (10**8)
            printConversion(numToConvert, convertedNum)
        case "kilometers":
            convertedNum = numToConvert / (10**9)
            printConversion(numToConvert, convertedNum)
        case "megameters":
            convertedNum = numToConvert / (10**12)
            printConversion(numToConvert, convertedNum)
        case "gigameters":
            convertedNum = numToConvert / (10**15)
            printConversion(numToConvert, convertedNum)
        case "terameters":
            convertedNum = numToConvert / (10**18)
            printConversion(numToConvert, convertedNum)
        case "inches":
            convertedNum = numToConvert * 0.0000393701
            printConversion(numToConvert, convertedNum)
        case "feet":
            convertedNum = numToConvert * 0.00000328084
            printConversion(numToConvert, convertedNum)
        case "yards":
            convertedNum = numToConvert * 0.000000109361
            printConversion(numToConvert, convertedNum)
        case "miles":
            convertedNum = numToConvert * 0.000000000621371
            printConversion(numToConvert, convertedNum)

def Millimeters(endingUnit):
    match endingUnit:
        case "picometers":
            convertedNum = numToConvert * (10**9)
            printConversion(numToConvert, convertedNum)
        case "nanometers":
            convertedNum = numToConvert * (10**6)
            printConversion(numToConvert, convertedNum)
        case "micrometers":
            convertedNum = numToConvert * (10**3)
            printConversion(numToConvert, convertedNum)
        case "millimeters":
            convertedNum = numToConvert 
            printConversion(numToConvert, convertedNum)
        case "centimeters":
            convertedNum = numToConvert / (10)
            printConversion(numToConvert, convertedNum)
        case "decimeters":
            convertedNum = numToConvert / (10**2)
            printConversion(numToConvert, convertedNum)
        case "meters":
            convertedNum = numToConvert / (10**3)
            printConversion(numToConvert, convertedNum)
        case "decameters":
            convertedNum = numToConvert / (10**4)
            printConversion(numToConvert, convertedNum)
        case "hectometers":
            convertedNum = numToConvert / (10**5)
            printConversion(numToConvert, convertedNum)
        case "kilometers":
            convertedNum = numToConvert / (10**6)
            printConversion(numToConvert, convertedNum)
        case "megameters":
            convertedNum = numToConvert / (10**9)
            printConversion(numToConvert, convertedNum)
        case "gigameters":
            convertedNum = numToConvert / (10**12)
            printConversion(numToConvert, convertedNum)
        case "terameters":
            convertedNum = numToConvert / (10**15)
            printConversion(numToConvert, convertedNum)
        case "inches":
            convertedNum = numToConvert * 0.0393701
            printConversion(numToConvert, convertedNum)
        case "feet":
            convertedNum = numToConvert * 0.00328084
            printConversion(numToConvert, convertedNum)
        case "yards":
            convertedNum = numToConvert * 0.00109361
            printConversion(numToConvert, convertedNum)
        case "miles":
            convertedNum = numToConvert * 0.000000621371
            printConversion(numToConvert, convertedNum)

def Centimeters(endingUnit):
    match endingUnit:
        case "picometers":
            convertedNum = numToConvert * (10**10)
            printConversion(numToConvert, convertedNum)
        case "nanometers":
            convertedNum = numToConvert * (10**7)
            printConversion(numToConvert, convertedNum)
        case "micrometers":
            convertedNum = numToConvert * (10**4)
            printConversion(numToConvert, convertedNum)
        case "millimeters":
            convertedNum = numToConvert * (10)
            printConversion(numToConvert, convertedNum)
        case "centimeters":
            convertedNum = numToConvert 
            printConversion(numToConvert, convertedNum)
        case "decimeters":
            convertedNum = numToConvert / (10)
            printConversion(numToConvert, convertedNum)
        case "meters":
            convertedNum = numToConvert / (10**2)
            printConversion(numToConvert, convertedNum)
        case "decameters":
            convertedNum = numToConvert / (10**3)
            printConversion(numToConvert, convertedNum)
        case "hectometers":
            convertedNum = numToConvert / (10**4)
            printConversion(numToConvert, convertedNum)
        case "kilometers":
            convertedNum = numToConvert / (10**5)
            printConversion(numToConvert, convertedNum)
        case "megameters":
            convertedNum = numToConvert / (10**8)
            printConversion(numToConvert, convertedNum)
        case "gigameters":
            convertedNum = numToConvert / (10**11)
            printConversion(numToConvert, convertedNum)
        case "terameters":
            convertedNum = numToConvert / (10**14)
            printConversion(numToConvert, convertedNum)
        case "inches":
            convertedNum = numToConvert * 0.393701
            printConversion(numToConvert, convertedNum)
        case "feet":
            convertedNum = numToConvert * 0.0328084
            printConversion(numToConvert, convertedNum)
        case "yards":
            convertedNum = numToConvert * 0.0109361
            printConversion(numToConvert, convertedNum)
        case "miles":
            convertedNum = numToConvert * 0.00000621371
            printConversion(numToConvert, convertedNum)

def Decimeters(endingUnit):
    match endingUnit:
        case "picometers":
            convertedNum = numToConvert * (10**11)
            printConversion(numToConvert, convertedNum)
        case "nanometers":
            convertedNum = numToConvert * (10**8)
            printConversion(numToConvert, convertedNum)
        case "micrometers":
            convertedNum = numToConvert * (10**7)
            printConversion(numToConvert, convertedNum)
        case "millimeters":
            convertedNum = numToConvert * (10**2)
            printConversion(numToConvert, convertedNum)
        case "centimeters":
            convertedNum = numToConvert * (10)
            printConversion(numToConvert, convertedNum)
        case "decimeters":
            convertedNum = numToConvert 
            printConversion(numToConvert, convertedNum)
        case "meters":
            convertedNum = numToConvert / (10)
            printConversion(numToConvert, convertedNum)
        case "decameters":
            convertedNum = numToConvert / (10**2)
            printConversion(numToConvert, convertedNum)
        case "hectometers":
            convertedNum = numToConvert / (10**3)
            printConversion(numToConvert, convertedNum)
        case "kilometers":
            convertedNum = numToConvert / (10**4)
            printConversion(numToConvert, convertedNum)
        case "megameters":
            convertedNum = numToConvert / (10**7)
            printConversion(numToConvert, convertedNum)
        case "gigameters":
            convertedNum = numToConvert / (10**10)
            printConversion(numToConvert, convertedNum)
        case "terameters":
            convertedNum = numToConvert / (10**13)
            printConversion(numToConvert, convertedNum)
        case "inches":
            convertedNum = numToConvert * 3.93701
            printConversion(numToConvert, convertedNum)
        case "feet":
            convertedNum = numToConvert * 0.328084
            printConversion(numToConvert, convertedNum)
        case "yards":
            convertedNum = numToConvert * 0.109361
            printConversion(numToConvert, convertedNum)
        case "miles":
            convertedNum = numToConvert * 0.0000621371
            printConversion(numToConvert, convertedNum)

def Meters(endingUnit):
    match endingUnit:
        case "picometers":
            convertedNum = numToConvert * (10**12)
            printConversion(numToConvert, convertedNum)
        case "nanometers":
            convertedNum = numToConvert * (10**9)
            printConversion(numToConvert, convertedNum)
        case "micrometers":
            convertedNum = numToConvert * (10**6)
            printConversion(numToConvert, convertedNum)
        case "millimeters":
            convertedNum = numToConvert * (10**3)
            printConversion(numToConvert, convertedNum)
        case "centimeters":
            convertedNum = numToConvert * (10**2)
            printConversion(numToConvert, convertedNum)
        case "decimeters":
            convertedNum = numToConvert * (10**1)
            printConversion(numToConvert, convertedNum)
        case "meters":
            convertedNum = numToConvert
            printConversion(numToConvert, convertedNum)
        case "decameters":
            convertedNum = numToConvert / (10**1)
            printConversion(numToConvert, convertedNum)
        case "hectometers":
            convertedNum = numToConvert / (10**2)
            printConversion(numToConvert, convertedNum)
        case "kilometers":
            convertedNum = numToConvert / (10**3)
            printConversion(numToConvert, convertedNum)
        case "megameters":
            convertedNum = numToConvert / (10**6)
            printConversion(numToConvert, convertedNum)
        case "gigameters":
            convertedNum = numToConvert / (10**9)
            printConversion(numToConvert, convertedNum)
        case "terameters":
            convertedNum = numToConvert / (10**12)
            printConversion(numToConvert, convertedNum)
        case "inches":
            convertedNum = numToConvert * 39.3701
            printConversion(numToConvert, convertedNum)
        case "feet":
            convertedNum = numToConvert * 3.28084
            printConversion(numToConvert, convertedNum)
        case "yards":
            convertedNum = numToConvert * 1.09361
            printConversion(numToConvert, convertedNum)
        case "miles":
            convertedNum = numToConvert * 0.000621371
            printConversion(numToConvert, convertedNum)
        
def Decameters(endingUnit):
    match endingUnit:
        case "picometers":
            convertedNum = numToConvert * (10**13)
            printConversion(numToConvert, convertedNum)
        case "nanometers":
            convertedNum = numToConvert * (10**8)
            printConversion(numToConvert, convertedNum)
        case "micrometers":
            convertedNum = numToConvert * (10**7)
            printConversion(numToConvert, convertedNum)
        case "millimeters":
            convertedNum = numToConvert * (10**4)
            printConversion(numToConvert, convertedNum)
        case "centimeters":
            convertedNum = numToConvert * (10**3)
            printConversion(numToConvert, convertedNum)
        case "decimeters":
            convertedNum = numToConvert * (10**2)
            printConversion(numToConvert, convertedNum)
        case "meters":
            convertedNum = numToConvert * 10
            printConversion(numToConvert, convertedNum)
        case "decameters":
            convertedNum = numToConvert 
            printConversion(numToConvert, convertedNum)
        case "hectometers":
            convertedNum = numToConvert / (10**1)
            printConversion(numToConvert, convertedNum)
        case "kilometers":
            convertedNum = numToConvert / (10**2)
            printConversion(numToConvert, convertedNum)
        case "megameters":
            convertedNum = numToConvert / (10**5)
            printConversion(numToConvert, convertedNum)
        case "gigameters":
            convertedNum = numToConvert / (10**8)
            printConversion(numToConvert, convertedNum)
        case "terameters":
            convertedNum = numToConvert / (10**11)
            printConversion(numToConvert, convertedNum)
        case "inches":
            convertedNum = numToConvert * 393.701
            printConversion(numToConvert, convertedNum)
        case "feet":
            convertedNum = numToConvert * 32.8084
            printConversion(numToConvert, convertedNum)
        case "yards":
            convertedNum = numToConvert * 10.9361
            printConversion(numToConvert, convertedNum)
        case "miles":
            convertedNum = numToConvert * 0.00621371
            printConversion(numToConvert, convertedNum)

def Hectometers(endingUnit):
    match endingUnit:
        case "picometers":
            convertedNum = numToConvert * (10**14)
            printConversion(numToConvert, convertedNum)
        case "nanometers":
            convertedNum = numToConvert * (10**11)
            printConversion(numToConvert, convertedNum)
        case "micrometers":
            convertedNum = numToConvert * (10**8)
            printConversion(numToConvert, convertedNum)
        case "millimeters":
            convertedNum = numToConvert * (10**5)
            printConversion(numToConvert, convertedNum)
        case "centimeters":
            convertedNum = numToConvert * (10**4)
            printConversion(numToConvert, convertedNum)
        case "decimeters":
            convertedNum = numToConvert * (10**3)
            printConversion(numToConvert, convertedNum)
        case "meters":
            convertedNum = numToConvert * (10**2)
            printConversion(numToConvert, convertedNum)
        case "decameters":
            convertedNum = numToConvert * (10**1)
            printConversion(numToConvert, convertedNum)
        case "hectometers":
            convertedNum = numToConvert
            printConversion(numToConvert, convertedNum)
        case "kilometers":
            convertedNum = numToConvert / (10**1)
            printConversion(numToConvert, convertedNum)
        case "megameters":
            convertedNum = numToConvert / (10**4)
            printConversion(numToConvert, convertedNum)
        case "gigameters":
            convertedNum = numToConvert / (10**7)
            printConversion(numToConvert, convertedNum)
        case "terameters":
            convertedNum = numToConvert / (10**10)
            printConversion(numToConvert, convertedNum)
        case "inches":
            convertedNum = numToConvert * 3937.01
            printConversion(numToConvert, convertedNum)
        case "feet":
            convertedNum = numToConvert * 328.084
            printConversion(numToConvert, convertedNum)
        case "yards":
            convertedNum = numToConvert * 109.361
            printConversion(numToConvert, convertedNum)
        case "miles":
            convertedNum = numToConvert * 0.0621371
            printConversion(numToConvert, convertedNum)

def Kilometers(endingUnit):
    match endingUnit:
        case "picometers":
            convertedNum = numToConvert * (10**15)
            printConversion(numToConvert, convertedNum)
        case "nanometers":
            convertedNum = numToConvert * (10**12)
            printConversion(numToConvert, convertedNum)
        case "micrometers":
            convertedNum = numToConvert * (10**9)
            printConversion(numToConvert, convertedNum)
        case "millimeters":
            convertedNum = numToConvert * (10**6)
            printConversion(numToConvert, convertedNum)
        case "centimeters":
            convertedNum = numToConvert * (10**5)
            printConversion(numToConvert, convertedNum)
        case "decimeters":
            convertedNum = numToConvert * (10**4)
            printConversion(numToConvert, convertedNum)
        case "meters":
            convertedNum = numToConvert * (10**3)
            printConversion(numToConvert, convertedNum)
        case "decameters":
            convertedNum = numToConvert * (10**2)
            printConversion(numToConvert, convertedNum)
        case "hectometers":
            convertedNum = numToConvert * (10**1)
            printConversion(numToConvert, convertedNum)
        case "kilometers":
            convertedNum = numToConvert
            printConversion(numToConvert, convertedNum)
        case "megameters":
            convertedNum = numToConvert / (10**3)
            printConversion(numToConvert, convertedNum)
        case "gigameters":
            convertedNum = numToConvert / (10**6)
            printConversion(numToConvert, convertedNum)
        case "terameters":
            convertedNum = numToConvert / (10**9)
            printConversion(numToConvert, convertedNum)
        case "inches":
            convertedNum = numToConvert * 39370.07874
            printConversion(numToConvert, convertedNum)
        case "feet":
            convertedNum = numToConvert * 3280.839895
            printConversion(numToConvert, convertedNum)
        case "yards":
            convertedNum = numToConvert * 1093.6132983
            printConversion(numToConvert, convertedNum)
        case "miles":
            convertedNum = numToConvert * 0.6213711922
            printConversion(numToConvert, convertedNum)

def Megameters(endingUnit):
    match endingUnit:
        case "picometers":
            convertedNum = numToConvert * (10**18)
            printConversion(numToConvert, convertedNum)
        case "nanometers":
            convertedNum = numToConvert * (10**15)
            printConversion(numToConvert, convertedNum)
        case "micrometers":
            convertedNum = numToConvert * (10**12)
            printConversion(numToConvert, convertedNum)
        case "millimeters":
            convertedNum = numToConvert * (10**9)
            printConversion(numToConvert, convertedNum)
        case "centimeters":
            convertedNum = numToConvert * (10**8)
            printConversion(numToConvert, convertedNum)
        case "decimeters":
            convertedNum = numToConvert * (10**7)
            printConversion(numToConvert, convertedNum)
        case "meters":
            convertedNum = numToConvert * (10**6)
            printConversion(numToConvert, convertedNum)
        case "decameters":
            convertedNum = numToConvert * (10**5)
            printConversion(numToConvert, convertedNum)
        case "hectometers":
            convertedNum = numToConvert * (10**4)
            printConversion(numToConvert, convertedNum)
        case "kilometers":
            convertedNum = numToConvert * (10**3)
            printConversion(numToConvert, convertedNum)
        case "megameters":
            convertedNum = numToConvert 
            printConversion(numToConvert, convertedNum)
        case "gigameters":
            convertedNum = numToConvert / (10**3)
            printConversion(numToConvert, convertedNum)
        case "terameters":
            convertedNum = numToConvert / (10**6)
            printConversion(numToConvert, convertedNum)
        case "inches":
            convertedNum = numToConvert * 39370787.4
            printConversion(numToConvert, convertedNum)
        case "feet":
            convertedNum = numToConvert * 3280839.895
            printConversion(numToConvert, convertedNum)
        case "yards":
            convertedNum = numToConvert * 1093613.2983
            printConversion(numToConvert, convertedNum)
        case "miles":
            convertedNum = numToConvert * 621.3711922
            printConversion(numToConvert, convertedNum)

def Gigameters(endingUnit):
    match endingUnit:
        case "picometers":
            convertedNum = numToConvert * (10**21)
            printConversion(numToConvert, convertedNum)
        case "nanometers":
            convertedNum = numToConvert * (10**18)
            printConversion(numToConvert, convertedNum)
        case "micrometers":
            convertedNum = numToConvert * (10**15)
            printConversion(numToConvert, convertedNum)
        case "millimeters":
            convertedNum = numToConvert * (10**12)
            printConversion(numToConvert, convertedNum)
        case "centimeters":
            convertedNum = numToConvert * (10**11)
            printConversion(numToConvert, convertedNum)
        case "decimeters":
            convertedNum = numToConvert * (10**10)
            printConversion(numToConvert, convertedNum)
        case "meters":
            convertedNum = numToConvert * (10**9)
            printConversion(numToConvert, convertedNum)
        case "decameters":
            convertedNum = numToConvert * (10**8)
            printConversion(numToConvert, convertedNum)
        case "hectometers":
            convertedNum = numToConvert * (10**7)
            printConversion(numToConvert, convertedNum)
        case "kilometers":
            convertedNum = numToConvert * (10**6)
            printConversion(numToConvert, convertedNum)
        case "megameters":
            convertedNum = numToConvert * (10**3)
            printConversion(numToConvert, convertedNum)
        case "gigameters":
            convertedNum = numToConvert
            printConversion(numToConvert, convertedNum)
        case "terameters":
            convertedNum = numToConvert / (10**3)
            printConversion(numToConvert, convertedNum)
        case "inches":
            convertedNum = numToConvert * 39370787400
            printConversion(numToConvert, convertedNum)
        case "feet":
            convertedNum = numToConvert * 3280839895
            printConversion(numToConvert, convertedNum)
        case "yards":
            convertedNum = numToConvert * 1093613298.3
            printConversion(numToConvert, convertedNum)
        case "miles":
            convertedNum = numToConvert * 621371.1922
            printConversion(numToConvert, convertedNum)

def Terameters(endingUnit):
    match endingUnit:
        case "picometers":
            convertedNum = numToConvert * (10**24)
            printConversion(numToConvert, convertedNum)
        case "nanometers":
            convertedNum = numToConvert * (10**21)
            printConversion(numToConvert, convertedNum)
        case "micrometers":
            convertedNum = numToConvert * (10**18)
            printConversion(numToConvert, convertedNum)
        case "millimeters":
            convertedNum = numToConvert * (10**15)
            printConversion(numToConvert, convertedNum)
        case "centimeters":
            convertedNum = numToConvert * (10**14)
            printConversion(numToConvert, convertedNum)
        case "decimeters":
            convertedNum = numToConvert * (10**13)
            printConversion(numToConvert, convertedNum)
        case "meters":
            convertedNum = numToConvert * (10**12)
            printConversion(numToConvert, convertedNum)
        case "decameters":
            convertedNum = numToConvert * (10**11)
            printConversion(numToConvert, convertedNum)
        case "hectometers":
            convertedNum = numToConvert * (10**10)
            printConversion(numToConvert, convertedNum)
        case "kilometers":
            convertedNum = numToConvert * (10**9)
            printConversion(numToConvert, convertedNum)
        case "megameters":
            convertedNum = numToConvert * (10**6)
            printConversion(numToConvert, convertedNum)
        case "gigameters":
            convertedNum = numToConvert * (10**3)
            printConversion(numToConvert, convertedNum)
        case "terameters":
            convertedNum = numToConvert
            printConversion(numToConvert, convertedNum)
        case "inches":
            convertedNum = numToConvert * 39370787400000
            printConversion(numToConvert, convertedNum)
        case "feet":
            convertedNum = numToConvert * 3280839895000
            printConversion(numToConvert, convertedNum)
        case "yards":
            convertedNum = numToConvert * 1093613298300
            printConversion(numToConvert, convertedNum)
        case "miles":
            convertedNum = numToConvert * 621371192.2
            printConversion(numToConvert, convertedNum)

# Imperial Conversion Functions #
def Inches(endingUnit):
    match endingUnit:
            case "picometers":
                convertedNum = numToConvert * 25400000000
                printConversion(numToConvert, convertedNum)
            case "nanometers":
                convertedNum = numToConvert * 25400000
                printConversion(numToConvert, convertedNum)
            case "micrometers":
                convertedNum = numToConvert * 25400
                printConversion(numToConvert, convertedNum)
            case "millimeters":
                convertedNum = numToConvert * 25.4
                printConversion(numToConvert, convertedNum)
            case "centimeters":
                convertedNum = numToConvert * 2.54
                printConversion(numToConvert, convertedNum)
            case "decimeters":
                convertedNum = numToConvert * 0.254
                printConversion(numToConvert, convertedNum)
            case "meters":
                convertedNum = numToConvert * 0.0254
                printConversion(numToConvert, convertedNum)
            case "decameters":
                convertedNum = numToConvert * 0.00254
                printConversion(numToConvert, convertedNum)
            case "hectometers":
                convertedNum = numToConvert * 0.000254
                printConversion(numToConvert, convertedNum)
            case "kilometers":
                convertedNum = numToConvert * 0.0000254
                printConversion(numToConvert, convertedNum)
            case "megameters":
                convertedNum = numToConvert * 0.0000000254
                printConversion(numToConvert, convertedNum)
            case "gigameters":
                convertedNum = numToConvert * 0.000000000254
                printConversion(numToConvert, convertedNum)
            case "terameters":
                convertedNum = numToConvert * 0.000000000000254
                printConversion(numToConvert, convertedNum)
            case "inches":
                convertedNum = numToConvert
                printConversion(numToConvert, convertedNum)
            case "feet":
                convertedNum = numToConvert * 0.0833333333 
                printConversion(numToConvert, convertedNum)
            case "yards":
                convertedNum = numToConvert * 0.0277777778
                printConversion(numToConvert, convertedNum)
            case "miles":
                convertedNum = numToConvert * 0.0000157828
                printConversion(numToConvert, convertedNum)

def Feet(endingUnit):
    match endingUnit:
            case "picometers":
                convertedNum = numToConvert * 25400000000 * 12
                printConversion(numToConvert, convertedNum)
            case "nanometers":
                convertedNum = numToConvert * 25400000 * 12
                printConversion(numToConvert, convertedNum)
            case "micrometers":
                convertedNum = numToConvert * 25400 * 12
                printConversion(numToConvert, convertedNum)
            case "millimeters":
                convertedNum = numToConvert * 25.4 * 12
                printConversion(numToConvert, convertedNum)
            case "centimeters":
                convertedNum = numToConvert * 2.54 * 12
                printConversion(numToConvert, convertedNum)
            case "decimeters":
                convertedNum = numToConvert * 0.254 * 12
                printConversion(numToConvert, convertedNum)
            case "meters":
                convertedNum = numToConvert * 0.0254 * 12
                printConversion(numToConvert, convertedNum)
            case "decameters":
                convertedNum = numToConvert * 0.00254 * 12
                printConversion(numToConvert, convertedNum)
            case "hectometers":
                convertedNum = numToConvert * 0.000254 * 12
                printConversion(numToConvert, convertedNum)
            case "kilometers":
                convertedNum = numToConvert * 0.0000254 * 12
                printConversion(numToConvert, convertedNum)
            case "megameters":
                convertedNum = numToConvert * 0.0000000254 * 12
                printConversion(numToConvert, convertedNum)
            case "gigameters":
                convertedNum = numToConvert * 0.000000000254 * 12
                printConversion(numToConvert, convertedNum)
            case "terameters":
                convertedNum = numToConvert * 0.000000000000254 * 12
                printConversion(numToConvert, convertedNum)
            case "inches":
                convertedNum = numToConvert * 12
                printConversion(numToConvert, convertedNum)
            case "feet":
                convertedNum = numToConvert 
                printConversion(numToConvert, convertedNum)
            case "yards":
                convertedNum = numToConvert / 3
                printConversion(numToConvert, convertedNum)
            case "miles":
                convertedNum = numToConvert / 5280
                printConversion(numToConvert, convertedNum)

def Yards(endingUnit):
    match endingUnit:
            case "picometers":
                convertedNum = numToConvert * 304800000000 * 12 * 3
                printConversion(numToConvert, convertedNum)
            case "nanometers":
                convertedNum = numToConvert * 25400000 * 12 * 3
                printConversion(numToConvert, convertedNum)
            case "micrometers":
                convertedNum = numToConvert * 25400 * 12 * 3
                printConversion(numToConvert, convertedNum)
            case "millimeters":
                convertedNum = numToConvert * 25.4 * 12 * 3
                printConversion(numToConvert, convertedNum)
            case "centimeters":
                convertedNum = numToConvert * 2.54 * 12 * 3 
                printConversion(numToConvert, convertedNum)
            case "decimeters":
                convertedNum = numToConvert * 0.254 * 12 * 3
                printConversion(numToConvert, convertedNum)
            case "meters":
                convertedNum = numToConvert * 0.0254 * 12 * 3
                printConversion(numToConvert, convertedNum)
            case "decameters":
                convertedNum = numToConvert * 0.00254 * 12 * 3
                printConversion(numToConvert, convertedNum)
            case "hectometers":
                convertedNum = numToConvert * 0.000254 * 12 * 3
                printConversion(numToConvert, convertedNum)
            case "kilometers":
                convertedNum = numToConvert * 0.0000254 * 12 * 3
                printConversion(numToConvert, convertedNum)
            case "megameters":
                convertedNum = numToConvert * 0.0000000254 * 12 * 3
                printConversion(numToConvert, convertedNum)
            case "gigameters":
                convertedNum = numToConvert * 0.000000000254 * 12 * 3
                printConversion(numToConvert, convertedNum)
            case "terameters":
                convertedNum = numToConvert * 0.000000000000254 * 12 * 3
                printConversion(numToConvert, convertedNum)
            case "inches":
                convertedNum = numToConvert * 12 * 3
                printConversion(numToConvert, convertedNum)
            case "feet":
                convertedNum = numToConvert * 3
                printConversion(numToConvert, convertedNum)
            case "yards":
                convertedNum = numToConvert 
                printConversion(numToConvert, convertedNum)
            case "miles":
                convertedNum = numToConvert * 0.0005681818
                printConversion(numToConvert, convertedNum)

def Miles(endingUnit):
    match endingUnit:
            case "picometers":
                convertedNum = numToConvert * 1609344000000010
                printConversion(numToConvert, convertedNum)
            case "nanometers":
                convertedNum = numToConvert * 1609344000000
                printConversion(numToConvert, convertedNum)
            case "micrometers":
                convertedNum = numToConvert * 1609344000
                printConversion(numToConvert, convertedNum)
            case "millimeters":
                convertedNum = numToConvert * 1609344
                printConversion(numToConvert, convertedNum)
            case "centimeters":
                convertedNum = numToConvert * 160934.4
                printConversion(numToConvert, convertedNum)
            case "decimeters":
                convertedNum = numToConvert * 16093.44
                printConversion(numToConvert, convertedNum)
            case "meters":
                convertedNum = numToConvert * 1609.344
                printConversion(numToConvert, convertedNum)
            case "decameters":
                convertedNum = numToConvert * 160.9344
                printConversion(numToConvert, convertedNum)
            case "hectometers":
                convertedNum = numToConvert * 16.09344
                printConversion(numToConvert, convertedNum)
            case "kilometers":
                convertedNum = numToConvert * 1.609344
                printConversion(numToConvert, convertedNum)
            case "megameters":
                convertedNum = numToConvert * 0.001609344
                printConversion(numToConvert, convertedNum)
            case "gigameters":
                convertedNum = numToConvert * 0.0000016093
                printConversion(numToConvert, convertedNum)
            case "terameters":
                convertedNum = numToConvert * 0.00000000016093
                printConversion(numToConvert, convertedNum)
            case "inches":
                convertedNum = numToConvert * 12 * 5280
                printConversion(numToConvert, convertedNum)
            case "feet":
                convertedNum = numToConvert * 5280
                printConversion(numToConvert, convertedNum)
            case "yards":
                convertedNum = numToConvert 
                printConversion(numToConvert, convertedNum)
            case "miles":
                convertedNum = numToConvert
                printConversion(numToConvert, convertedNum)
    
# Helper Functions and Classes #
def printConversion(numToConvert, convertedNum):
    print("{:,.12f}({:.2e}) {} is equal to {:,.12f}({:.2e}) {}.".format(numToConvert, numToConvert, firstUnit, convertedNum, convertedNum, endUnit))
    if convertedNum == numToConvert:
        print("Whoop-dee-fucking-doo!\n")

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
###########################################################################

################################ BASE UNITS AND VARIABLES ################################
listMetricLength = ['Picometers', 'Nanometers', 'Micrometers', 'Millimeters', 'Centimeters', 'Decimeters', 'Meters', 'Decameter', 'Hectometer', 'Kilometers', 'Megameters', 'Gigameters', 'Terameters']
listMetricVolume = ['Picoliters', 'Nanoliters', 'Microliters', 'Milliliters', 'Centiliters', 'Deciliters', 'Liters', 'Decaliters', 'Hectoliters', 'Kiloliters', 'Megaliters', 'Gigaliters', 'Teraliters'] 
listMetricMass = ['Picograms', 'Nanograms', 'Micrograms', 'Milligrams', 'Centigrams', 'Decigrams', 'Grams', 'Decagrams', 'Hectograms', 'Tonnes', 'Kiltonnes', 'Megatonnes', 'Gigatonnes', 'Teratonnes'] 
listMetric = [listMetricLength, listMetricVolume, listMetricMass]

listMetricLengthGREEN = listMetricLength.copy()
listMetricVolumeGREEN = listMetricVolume.copy()
listMetricMassGREEN = listMetricMass.copy()
listMetricGREEN = [listMetricLengthGREEN, listMetricVolumeGREEN, listMetricMassGREEN]

listImperialLength = ['Inches', 'Feet', 'Yards', 'Miles']
listImperialVolume = ['Fluid Ounces', 'Pints', 'Quarts', 'Gallons']
listImperialMass = ['Drachms', 'Ounces', 'Pounds', 'Tons']
listImperial = [listImperialLength, listImperialVolume, listImperialMass]

listImperialLengthGREEN = listImperialLength.copy()
listImperialVolumeGREEN = listImperialVolume.copy()
listImperialMassGREEN = listImperialMass.copy()
listImperialGREEN = [listImperialLengthGREEN, listImperialVolumeGREEN, listImperialMassGREEN]

firstUnit = ""
endUnit = ""
numToConvert = 0.0
convertedNum = 0.0

for i in range(len(listImperialLengthGREEN)):
    listImperialLengthGREEN[i] = color.GREEN + str(listImperialLengthGREEN[i] + color.END)

for i in range(len(listMetricLengthGREEN)):
    listMetricLengthGREEN[i] = color.GREEN + str(listMetricLengthGREEN[i] + color.END)

         
##########################################################################################

################################ MAIN PROGRAM ################################
print(color.BOLD + color.YELLOW + "\nWELCOME TO " + color.BLUE + color.UNDERLINE + "BOBBY'S" + color.END + color.YELLOW + " INFAMOUS CONVERSION CALCULATOR!\n\n" + color.END + \
"Currently implemented conversions are " + color.GREEN + "GREEN. " + color.END + "Numbers have a precision of up/down to 10^12.\n" + \
"This is my first program using python. I know I can use a library for conversions but I want to practice a bit. Look at my code and let me know how I can be more efficient.\n\n" + color.END + \
color.CYAN + color.BOLD + color.UNDERLINE + "METRIC UNITS:\n" + color.END + \
color.YELLOW + "Length:" + color.END)
print(', '.join(str(item) for item in listMetricLengthGREEN))
print(color.YELLOW + "Volume:" + color.END) 
print(', '.join(str(item) for item in listMetricVolumeGREEN))
print(color.YELLOW + "Mass:" + color.END) 
print(', '.join(str(item) for item in listMetricMassGREEN))

print("\n\
" + color.CYAN + color.BOLD + color.UNDERLINE + "IMPERIAL UNITS:\n" + color.END + \
color.YELLOW + "Length:" + color.END) 
print(', '.join(str(item) for item in listImperialLengthGREEN))
print(color.YELLOW + "Volume:" + color.END) 
print(', '.join(str(item) for item in listImperialVolumeGREEN))
print(color.YELLOW + "Mass:" + color.END)  
print(', '.join(str(item) for item in listImperialMassGREEN))

firstUnit = str(input("What unit are you converting from?\n"))




if any(firstUnit in i for i in listMetric) or any(firstUnit in i for i in listImperial):
    firstUnit = firstUnit.lower()
    numToConvert = float(input("How many {} do you have?\n".format(firstUnit)))
    endUnit = input("What units do you want to convert to?\n")
    if any(endUnit in sublist for sublist in listMetric) or any(endUnit in sublist for sublist in listImperial):
        endUnit = endUnit.lower()
        match firstUnit:
            case "meters":
                Meters(endUnit)
            case "kilometers":
                Kilometers(endUnit)
    else:
        print("End unit not in conversion list")
else:
    print("Unit not in conversion list")
##############################################################################


