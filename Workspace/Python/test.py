from checks import *
result = test_addieren(1,1, 2)
print("addition funktioniert:", result)

def addieren (value, value1):
    return value + value1
def subtrahieren (value, value1):
    return value - value1
def multiplizieren (value, value1):
    return value * value1  
def dividieren (value, value1):
    if value1==0:
        return "error"
    return value / value1  
a = 10
b = 20

meinTest = dividieren(a,b)
funktioniert = test_dividieren(a,b, meinTest)
print("division funktioniert", funktioniert)

meinTest = addieren(a,b)
funktioniert = test_addieren(a,b, meinTest)
print("Addition funktioniert", funktioniert)

meinTest = multiplizieren(a,b)
funktioniert = test_multiplizieren(a,b, meinTest)
print("multiplikation funktioniert", funktioniert)

meinTest = subtrahieren(a,b)
funktioniert = test_subtrahieren(a,b, meinTest)
print("subtraktion funktioniert", funktioniert)