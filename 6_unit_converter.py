#Unit converter for SI: you can convert multiples, submultiples or units for the follow

import re
import math

#Symbols and powers
multiples = {"T":12, "G": 9, "M":6, "k":3, "h":2, "da":1, "d":-1, "c":-2, "m":-3, "\u03bc":-6, "n":-9, "p":-12}

print("-----------------")
print("Unit Converter")
print("-----------------")
origValue = input("Original amount (Ex. 14km):")
destUnit = input("Conversion unit (Ex. cm):")
number = float(re.sub(r"(\d+\.?\d*)\s*(\w+)", r"\1", origValue).strip())
mult = re.sub(r"(\d+\.?\d*)\s*(\w+)", r"\2", origValue).strip()
unit = mult[-1]
mult = mult[:-1]
if mult != "" and len(destUnit)>1:
    print("Result: " + str(number*math.pow(10,multiples[mult])/math.pow(10,multiples[destUnit[:-1]])) + destUnit) 
elif not len(destUnit)>1:
    print("Result: " + str(number*math.pow(10,multiples[mult])) + unit) 
else:
    print("Result: " + str(number*10**0) + unit) 
math.pow(2,3)