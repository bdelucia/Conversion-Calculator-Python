import math
################################ BASE UNITS AND VARIABLES ################################
firstUnit = ""
endUnit = ""
numToConvert = 0.1
convertedNum = 0.0
firstIsLength = False
firstIsVolume = False
firstIsVolume = False
endIsLength = False
endIsVolume = False
endIsVolume = False
# Helper Functions and Classes #
def printConversion(numToConvert, convertedNum, firstUnit, endUnit):
    print("{:,.12f}({:.2e}) {} is equal to {:,.12f}({:.2e}) {}.".format(numToConvert, numToConvert, firstUnit, convertedNum, convertedNum, endUnit))
    if convertedNum == numToConvert:
        print("Whoop-dee-fucking-doo!\n")

def anotherRun():
    firstUnit = str(input("What unit are you converting from? (type 0 to exit)\n"))
    if(firstUnit == "0"):
        print("Goodbye!")
    else: 
        main(firstUnit)

def firstUnitIsWhat(firstUnit):
    if firstUnit in listMetricLength or firstUnit in listImperialLength:
        return "Length"
    elif firstUnit in listMetricVolume or firstUnit in listImperialVolume:
        return "Volume"
    elif firstUnit in listMetricMass or firstUnit in listImperialMass:
        return "Mass"

def endUnitIsWhat(endUnit):
    if endUnit in listMetricLength or endUnit in listImperialLength:
            return "Length"
    elif endUnit in listMetricVolume or endUnit in listImperialVolume:
        return "Volume"
    elif endUnit in listMetricMass or endUnit in listImperialMass:
        return "Mass"
    
def lowercaseList(list):
    for i in range(len(list)):
        list[i] = list[i].lower()
    return list

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

# Lists of units of measurement #
listMetricLength = ['Picometers', 'Nanometers', 'Micrometers', 'Millimeters', 'Centimeters', 'Decimeters', 'Meters', 'Decameter', 'Hectometer', 'Kilometers', 'Megameters', 'Gigameters', 'Terameters']
listMetricVolume = ['Picoliters', 'Nanoliters', 'Microliters', 'Milliliters', 'Centiliters', 'Deciliters', 'Liters', 'Decaliters', 'Hectoliters', 'Kiloliters', 'Megaliters', 'Gigaliters', 'Teraliters'] 
listMetricMass = ['Picograms', 'Nanograms', 'Micrograms', 'Milligrams', 'Centigrams', 'Decigrams', 'Grams', 'Decagrams', 'Hectograms', 'Tonnes', 'Kiltonnes', 'Megatonnes', 'Gigatonnes', 'Teratonnes'] 
listMetricLower = [lowercaseList(listMetricLength), lowercaseList(listMetricVolume), lowercaseList(listMetricMass)] 
listMetric = [listMetricLength, listMetricVolume, listMetricMass]

listImperialLength = ['Inches', 'Feet', 'Yards', 'Miles']
listImperialVolume = ['Fluid Ounces', 'Pints', 'Quarts', 'Gallons']
listImperialMass = ['Drachms', 'Ounces', 'Pounds', 'Tons']
listImperialLower = [lowercaseList(listImperialLength), lowercaseList(listImperialVolume), lowercaseList(listImperialMass)] 
listImperial = [listImperialLength, listImperialVolume, listImperialMass]

# Copy of the lists that are displayed to the user in color based on whether their implementation is complete #
listMetricLengthGREEN = listMetricLength.copy()
listMetricVolumeGREEN = listMetricVolume.copy()
listMetricMassGREEN = listMetricMass.copy()
listMetricGREEN = [listMetricLengthGREEN, listMetricVolumeGREEN, listMetricMassGREEN]

listImperialLengthGREEN = listImperialLength.copy()
listImperialVolumeGREEN = listImperialVolume.copy()
listImperialMassGREEN = listImperialMass.copy()
listImperialGREEN = [listImperialLengthGREEN, listImperialVolumeGREEN, listImperialMassGREEN]

for i in range(len(listImperialLengthGREEN)):
    listImperialLengthGREEN[i] = color.GREEN + str(listImperialLengthGREEN[i] + color.END)

for i in range(len(listMetricLengthGREEN)):
    listMetricLengthGREEN[i] = color.GREEN + str(listMetricLengthGREEN[i] + color.END)

##########################################################################################

################################ FUNCTIONS AND CLASSES ################################
# Metric Conversion Functions #
def Picometers(numToConvert, convertedNum, firstUnit, endUnit):
    match endUnit:
        case "picometers":
            convertedNum = numToConvert 
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "nanometers":
            convertedNum = numToConvert / (10**3)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "micrometers":
            convertedNum = numToConvert / (10**6)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "millimeters":
            convertedNum = numToConvert / (10**9)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "centimeters":
            convertedNum = numToConvert / (10**10)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decimeters":
            convertedNum = numToConvert / (10**11)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "meters":
            convertedNum = numToConvert / (10**12)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decameters":
            convertedNum = numToConvert / (10**13)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "hectometers":
            convertedNum = numToConvert / (10**14)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "kilometers":
            convertedNum = numToConvert / (10**15)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "megameters":
            convertedNum = numToConvert / (10**18)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "gigameters":
            convertedNum = numToConvert / (10**21)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "terameters":
            convertedNum = numToConvert / (10**24)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "inches":
            convertedNum = numToConvert * 0.0000000000393701
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "feet":
            convertedNum = numToConvert * 0.00000000000328084
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "yards":
            convertedNum = numToConvert * 0.00000000000109361
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "miles":
            convertedNum = numToConvert * 0.000000000000000621371
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)

def Nanometers(numToConvert, convertedNum, firstUnit, endUnit):
    match endUnit:
        case "picometers":
            convertedNum = numToConvert * (10**3)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "nanometers":
            convertedNum = numToConvert 
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "micrometers":
            convertedNum = numToConvert / (10**3)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "millimeters":
            convertedNum = numToConvert / (10**6)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "centimeters":
            convertedNum = numToConvert / (10**7)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decimeters":
            convertedNum = numToConvert / (10**8)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "meters":
            convertedNum = numToConvert / (10**9)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decameters":
            convertedNum = numToConvert / (10**10)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "hectometers":
            convertedNum = numToConvert / (10**11)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "kilometers":
            convertedNum = numToConvert / (10**12)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "megameters":
            convertedNum = numToConvert / (10**15)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "gigameters":
            convertedNum = numToConvert / (10**18)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "terameters":
            convertedNum = numToConvert / (10**21)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "inches":
            convertedNum = numToConvert * 0.0000000393701
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "feet":
            convertedNum = numToConvert * 0.00000000328084
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "yards":
            convertedNum = numToConvert * 0.00000000109361
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "miles":
            convertedNum = numToConvert * 0.000000000000621371
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)

def Micrometers(numToConvert, convertedNum, firstUnit, endUnit):
    match endUnit:
        case "picometers":
            convertedNum = numToConvert * (10**6)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "nanometers":
            convertedNum = numToConvert * (10**3)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "micrometers":
            convertedNum = numToConvert 
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "millimeters":
            convertedNum = numToConvert / (10**3)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "centimeters":
            convertedNum = numToConvert / (10**4)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decimeters":
            convertedNum = numToConvert / (10**5)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "meters":
            convertedNum = numToConvert / (10**6)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decameters":
            convertedNum = numToConvert / (10**7)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "hectometers":
            convertedNum = numToConvert / (10**8)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "kilometers":
            convertedNum = numToConvert / (10**9)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "megameters":
            convertedNum = numToConvert / (10**12)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "gigameters":
            convertedNum = numToConvert / (10**15)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "terameters":
            convertedNum = numToConvert / (10**18)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "inches":
            convertedNum = numToConvert * 0.0000393701
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "feet":
            convertedNum = numToConvert * 0.00000328084
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "yards":
            convertedNum = numToConvert * 0.000000109361
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "miles":
            convertedNum = numToConvert * 0.000000000621371
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)

def Millimeters(numToConvert, convertedNum, firstUnit, endUnit):
    match endUnit:
        case "picometers":
            convertedNum = numToConvert * (10**9)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "nanometers":
            convertedNum = numToConvert * (10**6)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "micrometers":
            convertedNum = numToConvert * (10**3)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "millimeters":
            convertedNum = numToConvert 
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "centimeters":
            convertedNum = numToConvert / (10)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decimeters":
            convertedNum = numToConvert / (10**2)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "meters":
            convertedNum = numToConvert / (10**3)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decameters":
            convertedNum = numToConvert / (10**4)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "hectometers":
            convertedNum = numToConvert / (10**5)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "kilometers":
            convertedNum = numToConvert / (10**6)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "megameters":
            convertedNum = numToConvert / (10**9)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "gigameters":
            convertedNum = numToConvert / (10**12)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "terameters":
            convertedNum = numToConvert / (10**15)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "inches":
            convertedNum = numToConvert * 0.0393701
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "feet":
            convertedNum = numToConvert * 0.00328084
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "yards":
            convertedNum = numToConvert * 0.00109361
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "miles":
            convertedNum = numToConvert * 0.000000621371
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)

def Centimeters(numToConvert, convertedNum, firstUnit, endUnit):
    match endUnit:
        case "picometers":
            convertedNum = numToConvert * (10**10)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "nanometers":
            convertedNum = numToConvert * (10**7)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "micrometers":
            convertedNum = numToConvert * (10**4)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "millimeters":
            convertedNum = numToConvert * (10)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "centimeters":
            convertedNum = numToConvert 
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decimeters":
            convertedNum = numToConvert / (10)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "meters":
            convertedNum = numToConvert / (10**2)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decameters":
            convertedNum = numToConvert / (10**3)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "hectometers":
            convertedNum = numToConvert / (10**4)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "kilometers":
            convertedNum = numToConvert / (10**5)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "megameters":
            convertedNum = numToConvert / (10**8)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "gigameters":
            convertedNum = numToConvert / (10**11)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "terameters":
            convertedNum = numToConvert / (10**14)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "inches":
            convertedNum = numToConvert * 0.393701
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "feet":
            convertedNum = numToConvert * 0.0328084
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "yards":
            convertedNum = numToConvert * 0.0109361
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "miles":
            convertedNum = numToConvert * 0.00000621371
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)

def Decimeters(numToConvert, convertedNum, firstUnit, endUnit):
    match endUnit:
        case "picometers":
            convertedNum = numToConvert * (10**11)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "nanometers":
            convertedNum = numToConvert * (10**8)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "micrometers":
            convertedNum = numToConvert * (10**7)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "millimeters":
            convertedNum = numToConvert * (10**2)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "centimeters":
            convertedNum = numToConvert * (10)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decimeters":
            convertedNum = numToConvert 
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "meters":
            convertedNum = numToConvert / (10)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decameters":
            convertedNum = numToConvert / (10**2)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "hectometers":
            convertedNum = numToConvert / (10**3)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "kilometers":
            convertedNum = numToConvert / (10**4)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "megameters":
            convertedNum = numToConvert / (10**7)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "gigameters":
            convertedNum = numToConvert / (10**10)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "terameters":
            convertedNum = numToConvert / (10**13)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "inches":
            convertedNum = numToConvert * 3.93701
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "feet":
            convertedNum = numToConvert * 0.328084
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "yards":
            convertedNum = numToConvert * 0.109361
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "miles":
            convertedNum = numToConvert * 0.0000621371
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)

def Meters(numToConvert, convertedNum, firstUnit, endUnit):
    match endUnit:
        case "picometers":
            convertedNum = numToConvert * (10**12)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "nanometers":
            convertedNum = numToConvert * (10**9)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "micrometers":
            convertedNum = numToConvert * (10**6)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "millimeters":
            convertedNum = numToConvert * (10**3)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "centimeters":
            convertedNum = numToConvert * (10**2)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decimeters":
            convertedNum = numToConvert * (10**1)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "meters":
            convertedNum = numToConvert
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decameters":
            convertedNum = numToConvert / (10**1)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "hectometers":
            convertedNum = numToConvert / (10**2)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "kilometers":
            convertedNum = numToConvert / (10**3)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "megameters":
            convertedNum = numToConvert / (10**6)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "gigameters":
            convertedNum = numToConvert / (10**9)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "terameters":
            convertedNum = numToConvert / (10**12)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "inches":
            convertedNum = numToConvert * 39.3701
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "feet":
            convertedNum = numToConvert * 3.28084
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "yards":
            convertedNum = numToConvert * 1.09361
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "miles":
            convertedNum = numToConvert * 0.000621371
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        
def Decameters(numToConvert, convertedNum, firstUnit, endUnit):
    match endUnit:
        case "picometers":
            convertedNum = numToConvert * (10**13)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "nanometers":
            convertedNum = numToConvert * (10**8)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "micrometers":
            convertedNum = numToConvert * (10**7)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "millimeters":
            convertedNum = numToConvert * (10**4)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "centimeters":
            convertedNum = numToConvert * (10**3)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decimeters":
            convertedNum = numToConvert * (10**2)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "meters":
            convertedNum = numToConvert * 10
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decameters":
            convertedNum = numToConvert 
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "hectometers":
            convertedNum = numToConvert / (10**1)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "kilometers":
            convertedNum = numToConvert / (10**2)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "megameters":
            convertedNum = numToConvert / (10**5)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "gigameters":
            convertedNum = numToConvert / (10**8)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "terameters":
            convertedNum = numToConvert / (10**11)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "inches":
            convertedNum = numToConvert * 393.701
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "feet":
            convertedNum = numToConvert * 32.8084
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "yards":
            convertedNum = numToConvert * 10.9361
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "miles":
            convertedNum = numToConvert * 0.00621371
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)

def Hectometers(numToConvert, convertedNum, firstUnit, endUnit):
    match endUnit:
        case "picometers":
            convertedNum = numToConvert * (10**14)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "nanometers":
            convertedNum = numToConvert * (10**11)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "micrometers":
            convertedNum = numToConvert * (10**8)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "millimeters":
            convertedNum = numToConvert * (10**5)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "centimeters":
            convertedNum = numToConvert * (10**4)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decimeters":
            convertedNum = numToConvert * (10**3)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "meters":
            convertedNum = numToConvert * (10**2)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decameters":
            convertedNum = numToConvert * (10**1)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "hectometers":
            convertedNum = numToConvert
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "kilometers":
            convertedNum = numToConvert / (10**1)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "megameters":
            convertedNum = numToConvert / (10**4)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "gigameters":
            convertedNum = numToConvert / (10**7)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "terameters":
            convertedNum = numToConvert / (10**10)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "inches":
            convertedNum = numToConvert * 3937.01
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "feet":
            convertedNum = numToConvert * 328.084
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "yards":
            convertedNum = numToConvert * 109.361
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "miles":
            convertedNum = numToConvert * 0.0621371
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)

def Kilometers(numToConvert, convertedNum, firstUnit, endUnit):
    match endUnit:
        case "picometers":
            convertedNum = numToConvert * (10**15)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "nanometers":
            convertedNum = numToConvert * (10**12)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "micrometers":
            convertedNum = numToConvert * (10**9)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "millimeters":
            convertedNum = numToConvert * (10**6)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "centimeters":
            convertedNum = numToConvert * (10**5)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decimeters":
            convertedNum = numToConvert * (10**4)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "meters":
            convertedNum = numToConvert * (10**3)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decameters":
            convertedNum = numToConvert * (10**2)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "hectometers":
            convertedNum = numToConvert * (10**1)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "kilometers":
            convertedNum = numToConvert
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "megameters":
            convertedNum = numToConvert / (10**3)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "gigameters":
            convertedNum = numToConvert / (10**6)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "terameters":
            convertedNum = numToConvert / (10**9)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "inches":
            convertedNum = numToConvert * 39370.07874
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "feet":
            convertedNum = numToConvert * 3280.839895
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "yards":
            convertedNum = numToConvert * 1093.6132983
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "miles":
            convertedNum = numToConvert * 0.6213711922
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)

def Megameters(numToConvert, convertedNum, firstUnit, endUnit):
    match endUnit:
        case "picometers":
            convertedNum = numToConvert * (10**18)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "nanometers":
            convertedNum = numToConvert * (10**15)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "micrometers":
            convertedNum = numToConvert * (10**12)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "millimeters":
            convertedNum = numToConvert * (10**9)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "centimeters":
            convertedNum = numToConvert * (10**8)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decimeters":
            convertedNum = numToConvert * (10**7)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "meters":
            convertedNum = numToConvert * (10**6)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decameters":
            convertedNum = numToConvert * (10**5)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "hectometers":
            convertedNum = numToConvert * (10**4)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "kilometers":
            convertedNum = numToConvert * (10**3)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "megameters":
            convertedNum = numToConvert 
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "gigameters":
            convertedNum = numToConvert / (10**3)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "terameters":
            convertedNum = numToConvert / (10**6)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "inches":
            convertedNum = numToConvert * 39370787.4
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "feet":
            convertedNum = numToConvert * 3280839.895
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "yards":
            convertedNum = numToConvert * 1093613.2983
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "miles":
            convertedNum = numToConvert * 621.3711922
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)

def Gigameters(numToConvert, convertedNum, firstUnit, endUnit):
    match endUnit:
        case "picometers":
            convertedNum = numToConvert * (10**21)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "nanometers":
            convertedNum = numToConvert * (10**18)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "micrometers":
            convertedNum = numToConvert * (10**15)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "millimeters":
            convertedNum = numToConvert * (10**12)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "centimeters":
            convertedNum = numToConvert * (10**11)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decimeters":
            convertedNum = numToConvert * (10**10)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "meters":
            convertedNum = numToConvert * (10**9)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decameters":
            convertedNum = numToConvert * (10**8)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "hectometers":
            convertedNum = numToConvert * (10**7)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "kilometers":
            convertedNum = numToConvert * (10**6)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "megameters":
            convertedNum = numToConvert * (10**3)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "gigameters":
            convertedNum = numToConvert
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "terameters":
            convertedNum = numToConvert / (10**3)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "inches":
            convertedNum = numToConvert * 39370787400
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "feet":
            convertedNum = numToConvert * 3280839895
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "yards":
            convertedNum = numToConvert * 1093613298.3
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "miles":
            convertedNum = numToConvert * 621371.1922
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)

def Terameters(numToConvert, convertedNum, firstUnit, endUnit):
    match endUnit:
        case "picometers":
            convertedNum = numToConvert * (10**24)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "nanometers":
            convertedNum = numToConvert * (10**21)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "micrometers":
            convertedNum = numToConvert * (10**18)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "millimeters":
            convertedNum = numToConvert * (10**15)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "centimeters":
            convertedNum = numToConvert * (10**14)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decimeters":
            convertedNum = numToConvert * (10**13)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "meters":
            convertedNum = numToConvert * (10**12)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "decameters":
            convertedNum = numToConvert * (10**11)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "hectometers":
            convertedNum = numToConvert * (10**10)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "kilometers":
            convertedNum = numToConvert * (10**9)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "megameters":
            convertedNum = numToConvert * (10**6)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "gigameters":
            convertedNum = numToConvert * (10**3)
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "terameters":
            convertedNum = numToConvert
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "inches":
            convertedNum = numToConvert * 39370787400000
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "feet":
            convertedNum = numToConvert * 3280839895000
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "yards":
            convertedNum = numToConvert * 1093613298300
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)
        case "miles":
            convertedNum = numToConvert * 621371192.2
            printConversion(numToConvert, convertedNum, firstUnit, endUnit)

# Imperial Conversion Functions #
def Inches(numToConvert, convertedNum, firstUnit, endUnit):
    match endUnit:
            case "picometers":
                convertedNum = numToConvert * 25400000000
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "nanometers":
                convertedNum = numToConvert * 25400000
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "micrometers":
                convertedNum = numToConvert * 25400
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "millimeters":
                convertedNum = numToConvert * 25.4
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "centimeters":
                convertedNum = numToConvert * 2.54
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "decimeters":
                convertedNum = numToConvert * 0.254
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "meters":
                convertedNum = numToConvert * 0.0254
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "decameters":
                convertedNum = numToConvert * 0.00254
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "hectometers":
                convertedNum = numToConvert * 0.000254
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "kilometers":
                convertedNum = numToConvert * 0.0000254
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "megameters":
                convertedNum = numToConvert * 0.0000000254
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "gigameters":
                convertedNum = numToConvert * 0.000000000254
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "terameters":
                convertedNum = numToConvert * 0.000000000000254
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "inches":
                convertedNum = numToConvert
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "feet":
                convertedNum = numToConvert * 0.0833333333 
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "yards":
                convertedNum = numToConvert * 0.0277777778
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "miles":
                convertedNum = numToConvert * 0.0000157828
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)

def Feet(numToConvert, convertedNum, firstUnit, endUnit):
    match endUnit:
            case "picometers":
                convertedNum = numToConvert * 25400000000 * 12
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "nanometers":
                convertedNum = numToConvert * 25400000 * 12
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "micrometers":
                convertedNum = numToConvert * 25400 * 12
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "millimeters":
                convertedNum = numToConvert * 25.4 * 12
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "centimeters":
                convertedNum = numToConvert * 2.54 * 12
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "decimeters":
                convertedNum = numToConvert * 0.254 * 12
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "meters":
                convertedNum = numToConvert * 0.0254 * 12
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "decameters":
                convertedNum = numToConvert * 0.00254 * 12
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "hectometers":
                convertedNum = numToConvert * 0.000254 * 12
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "kilometers":
                convertedNum = numToConvert * 0.0000254 * 12
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "megameters":
                convertedNum = numToConvert * 0.0000000254 * 12
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "gigameters":
                convertedNum = numToConvert * 0.000000000254 * 12
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "terameters":
                convertedNum = numToConvert * 0.000000000000254 * 12
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "inches":
                convertedNum = numToConvert * 12
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "feet":
                convertedNum = numToConvert 
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "yards":
                convertedNum = numToConvert / 3
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "miles":
                convertedNum = numToConvert / 5280
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)

def Yards(numToConvert, convertedNum, firstUnit, endUnit):
    match endUnit:
            case "picometers":
                convertedNum = numToConvert * 304800000000 * 12 * 3
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "nanometers":
                convertedNum = numToConvert * 25400000 * 12 * 3
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "micrometers":
                convertedNum = numToConvert * 25400 * 12 * 3
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "millimeters":
                convertedNum = numToConvert * 25.4 * 12 * 3
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "centimeters":
                convertedNum = numToConvert * 2.54 * 12 * 3 
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "decimeters":
                convertedNum = numToConvert * 0.254 * 12 * 3
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "meters":
                convertedNum = numToConvert * 0.0254 * 12 * 3
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "decameters":
                convertedNum = numToConvert * 0.00254 * 12 * 3
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "hectometers":
                convertedNum = numToConvert * 0.000254 * 12 * 3
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "kilometers":
                convertedNum = numToConvert * 0.0000254 * 12 * 3
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "megameters":
                convertedNum = numToConvert * 0.0000000254 * 12 * 3
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "gigameters":
                convertedNum = numToConvert * 0.000000000254 * 12 * 3
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "terameters":
                convertedNum = numToConvert * 0.000000000000254 * 12 * 3
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "inches":
                convertedNum = numToConvert * 12 * 3
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "feet":
                convertedNum = numToConvert * 3
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "yards":
                convertedNum = numToConvert 
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "miles":
                convertedNum = numToConvert * 0.0005681818
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)

def Miles(numToConvert, convertedNum, firstUnit, endUnit):

    match endUnit:
            case "picometers":
                convertedNum = numToConvert * 1609344000000010
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "nanometers":
                convertedNum = numToConvert * 1609344000000
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "micrometers":
                convertedNum = numToConvert * 1609344000
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "millimeters":
                convertedNum = numToConvert * 1609344
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "centimeters":
                convertedNum = numToConvert * 160934.4
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "decimeters":
                convertedNum = numToConvert * 16093.44
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "meters":
                convertedNum = numToConvert * 1609.344
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "decameters":
                convertedNum = numToConvert * 160.9344
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "hectometers":
                convertedNum = numToConvert * 16.09344
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "kilometers":
                convertedNum = numToConvert * 1.609344
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "megameters":
                convertedNum = numToConvert * 0.001609344
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "gigameters":
                convertedNum = numToConvert * 0.0000016093
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "terameters":
                convertedNum = numToConvert * 0.00000000016093
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "inches":
                convertedNum = numToConvert * 12 * 5280
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "feet":
                convertedNum = numToConvert * 5280
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "yards":
                convertedNum = numToConvert 
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
            case "miles":
                convertedNum = numToConvert
                printConversion(numToConvert, convertedNum, firstUnit, endUnit)
    
   # Main program UI Function#

def main(firstUnit):
    if (any(firstUnit in i for i in listMetric) or any(firstUnit in i for i in listImperial)) or \
        (any(firstUnit.lower() in i for i in listMetricLower) or any(firstUnit.lower() in i for i in listImperialLower)):
        firstUnitCategory = firstUnitIsWhat(firstUnit)
        firstUnit = firstUnit.lower()
        numToConvert = float(input("How many {} do you have?\n".format(firstUnit)))
        
        endUnit = input("What units do you want to convert to?\n")
        if any(endUnit in sublist for sublist in listMetric) or any(endUnit in sublist for sublist in listImperial) or \
            (any(endUnit.lower() in i for i in listMetricLower) or any(endUnit.lower() in i for i in listImperialLower)):
            if(firstUnitCategory == endUnitIsWhat(endUnit)):
                endUnit = endUnit.lower()
                match firstUnit:
                    case "picometers":
                        Picometers(numToConvert, convertedNum, firstUnit, endUnit)
                        anotherRun()
                    case "nanometers":
                        Nanometers(numToConvert, convertedNum, firstUnit, endUnit)
                        anotherRun()
                    case "micrometers":
                        Micrometers(numToConvert, convertedNum, firstUnit, endUnit)
                        anotherRun()
                    case "millimeters":
                        Millimeters(numToConvert, convertedNum, firstUnit, endUnit)
                        anotherRun()
                    case "centimeters":
                        Centimeters(numToConvert, convertedNum, firstUnit, endUnit)
                        anotherRun()
                    case "decimeters":
                        Decimeters(numToConvert, convertedNum, firstUnit, endUnit)
                        anotherRun()
                    case "meters":
                        Meters(numToConvert, convertedNum, firstUnit, endUnit)
                        anotherRun()
                    case "decameters":
                        Decameters(numToConvert, convertedNum, firstUnit, endUnit)
                        anotherRun()
                    case "hectometers":
                        Hectometers(numToConvert, convertedNum, firstUnit, endUnit)
                        anotherRun()
                    case "kilometers":
                        Kilometers(numToConvert, convertedNum, firstUnit, endUnit)
                        anotherRun()
                    case "megameters":
                        Megameters(numToConvert, convertedNum, firstUnit, endUnit)
                        anotherRun()
                    case "gigameters":
                        Gigameters(numToConvert, convertedNum, firstUnit, endUnit)
                        anotherRun()
                    case "terameters":
                        Terameters(numToConvert, convertedNum, firstUnit, endUnit)
                        anotherRun()
                    case "inches":
                        Inches(numToConvert, convertedNum, firstUnit, endUnit)
                        anotherRun()
                    case "feet":
                        Feet(numToConvert, convertedNum, firstUnit, endUnit)
                        anotherRun()
                    case "yards":
                        Yards(numToConvert, convertedNum, firstUnit, endUnit)
                        anotherRun()
                    case "miles":
                        Miles(numToConvert, convertedNum, firstUnit, endUnit)
                        anotherRun()
            else:
                print("Units do not share categories.\n")
                anotherRun()
        else:
            print("End unit not in conversion list")
    else:
        print("Unit not in conversion list")
###########################################################################

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

firstUnit = str(input("What unit are you converting from? (type 0 to exit)\n"))
main(firstUnit)
##############################################################################


