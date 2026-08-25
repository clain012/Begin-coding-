while True:
    try:
        Temperature = float(input("Your temperature? "))
        break
    except ValueError:
        print ("Enter a number ...? ")
print ("Now: ",Temperature )

while True:
    unit = input("To Kelvin(K) or Fahrenheit(F)? ").upper()
    if unit in ("K","F"):
        break
    print ("Either enter K or F: ")

if unit == "K":
    converter = Temperature + 273.15
    print ("Temperature in Kelvin: ",converter)
elif unit == "F":
    converter = Temperature*1.8 +32
    print ("Temperature in Fahrenheit: " ,converter)

while True:
    Health_side = input("Would you like to continue to the health side of that temperature,'Yes' or 'No'? ").lower()
    if Health_side in ("yes",):
        break
    print ("please agree")

temp1 = Temperature
if temp1 < 35:
    print("Patient 1: Hypothermia - seek care")
elif 35 <= temp1 < 36.1:
    print("Patient 1: Slightly low")
elif 36.1 <= temp1 <= 37.2:
    print("Patient 1: Normal")
elif 37.2 < temp1 < 38:
    print("Patient 1: Slightly elevated")
elif 38 <= temp1 < 39:
    print("Patient 1: Low-grade fever")
elif 39 <= temp1 < 40:
    print("Patient 1: High fever")
else:
    print("Patient 1: Very high - seek medical care")

