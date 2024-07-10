import math

def header():
  print("""--------------------------------------------
                  \n          Calculator Program\n
---------------------------------------------\n""")
  print("Select the number 0 to exit the program\n")

  operations = ["Addition", "Subtraction", "Multiplication", "Division", "Square Root", "Cube Root", "Exponents"]

  number = 0

  for operation in operations:
    number += 1
    print(number,".", operation)

def clearScreen():
  print("\033[H\033[J", end="")

def addition():
  addnum1 = float(input("\nPlease input the first number: "))
  addnum2 = float(input("\nPlease input the second number: "))
  sum = addnum1 + addnum2
  print("\n",addnum1, "+", addnum2, "=", sum)

def subtraction():
  subnum1 = float(input("\nPlease input the first number: "))
  subnum2 = float(input("\nPlease input the second number: "))
  dif = subnum1 - subnum2
  print("\n",subnum1, "-", subnum2, "=", dif)

def multiplication():
  multnum1 = float(input("\nPlease input the first number: "))
  multnum2 = float(input("\nPlease input the second number: "))
  product = multnum1 * multnum1
  print("\n",multnum1, "x", multnum2, "=", product)
  
def division():
  divnum1 = float(input("\nPlease input the first number: "))
  divnum2 = float(input("\nPlease input the second number: "))
  
  if divnum2 == 0:
    print("\nDivision by zero will be undefined")

  else:
    quotient = divnum1 / divnum2
    print("\n", divnum1, "/", divnum2, "=", quotient)

def squareRoot():
  sqrtnum = float(input("\nPlease input the number you want to square root: "))

  if sqrtnum < 0:
    print("\nSquare roots with negative numbers are undefined")
    anotherOperation()

  else:
    root = math.sqrt(sqrtnum)

    print("\nThe square root of", sqrtnum, "is", root)

def cubeRoot():
  cubenum = float(input("\nPlease input the number you want to cube root: "))
  cubert = cubenum ** (1/3)
  print("\nThe square root of", cubenum, "is", cubert)

def exponents():
  base = float(input("\nPlease input the base number: "))
  power = float(input("\nPlease input the power: "))
  exponential = base ** power
  print("\n",base,"**", power, "=", exponential)

def anotherOperation():
  input("\nPress enter to perform another operation or select the number 0 to exit the program ")

calculation = True

while calculation:
  clearScreen()
  header()
  whatOperation = input("\nPlease select the number that corresponds to the operation you want to perform: ")

  if whatOperation == "1":
    addition()
    anotherOperation()

  elif whatOperation == "2":
    subtraction()
    anotherOperation()

  elif whatOperation == "3":
    multiplication()
    anotherOperation()

  elif whatOperation == "4":
    division()
    anotherOperation()

  elif whatOperation == "5":
    squareRoot()
    anotherOperation()

  elif whatOperation == "6":
    cubeRoot()
    anotherOperation()
  
  elif whatOperation == "7":
    exponents()
    anotherOperation()
  
  elif whatOperation == "0":
    calculation = False

  else:
    print("This is not a valid option.")
    anotherOperation()

print("Thank you for using this calculator. Have a nice day!")
