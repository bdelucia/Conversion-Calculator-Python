import math
################################ FUNCTIONS AND CLASSES ################################
# Conversion Functions #
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
   ITALICS = '\033[3m'
   END = '\033[0m'
###########################################################################

################################ BASE UNITS AND VARIABLES ################################
listMetricLength = ['Picometers', 'Nanometers', 'Micrometers', 'Millimeters', 'Centimeters', 'Decimeters', 'Meters', 'Dekameter', 'Hectometer', 'Kilometers', 'Megameters', 'Gigameters', 'Terameters']
listMetricVolume = ['Picoliters', 'Nanoliters', 'Microliters', 'Milliliters', 'Centiliters', 'Deciliters', 'Liters', 'Dekaliters', 'Hectoliters', 'Kiloliters', 'Megaliters', 'Gigaliters', 'Teraliters'] 
listMetricMass = ['Picograms', 'Nanograms', 'Micrograms', 'Milligrams', 'Centigrams', 'Decigrams', 'Grams', 'Dekagrams', 'Hectograms', 'Tonnes', 'Kiltonnes', 'Megatonnes', 'Gigatonnes', 'Teratonnes'] 
listMetric = [listMetricLength, listMetricVolume, listMetricMass]
              
              
listImperialLength = ['Inches', 'Feet', 'Yards', 'Miles']
listImperialVolume = ['Fluid Ounces', 'Pints', 'Quarts', 'Gallons']
listImperialMass = ['Drachms', 'Ounces', 'Pounds', 'Tons']
listImperial = [listImperialLength, listImperialVolume, listImperialMass]

firstUnit = ""
endUnit = ""
numToConvert = 0.0
convertedNum = 0.0

for i in range(len(listMetricLength)):
    if listMetricLength[i] == "Meters":
        listMetricLength[i] = color.GREEN + str(listMetricLength[i]) + color.END
    if listMetricLength[i] == "Kilometers":
        listMetricLength[i] = color.GREEN + str(listMetricLength[i]) + color.END
         
##########################################################################################

################################ MAIN PROGRAM ################################
print(color.BOLD + color.YELLOW + "\nWELCOME TO " + color.BLUE + color.UNDERLINE + "BOBBY'S" + color.END + color.YELLOW + " INFAMOUS CONVERSION CALCULATOR!\n" + color.END + \
color.ITALICS + "Currently implemented conversions are " + color.GREEN + "GREEN. " + color.END + color.ITALICS + "Numbers have a precision of up/down to 10^12.\n" + \
"This is my first program using python. I know I can use a library for conversions but I want to practice a bit. Look at my code and let me know how I can be more efficient.\n" + color.END + \
color.CYAN + color.BOLD + color.UNDERLINE + "METRIC UNITS:\n" + color.END + \
"Length: ")
print(', '.join(str(item) for item in listMetricLength))
print("Volume: ") 
print(', '.join(str(item) for item in listMetricVolume))
print("Mass: ") 
print(', '.join(str(item) for item in listMetricMass))

print("\n\
" + color.CYAN + color.BOLD + color.UNDERLINE + "IMPERIAL UNITS:\n" + color.END + \
"Length: ") 
print(', '.join(str(item) for item in listImperialLength))
print("Volume: ") 
print(', '.join(str(item) for item in listImperialVolume))
print("Mass: ") 
print(', '.join(str(item) for item in listImperialMass))


firstUnit = input("What unit are you converting from?\n")


if any(firstUnit in sublist for sublist in listMetric) or any(firstUnit in sublist for sublist in listImperial):
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


