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
    print ("please agree solely: ")

temp1 = Temperature
if temp1 < 35:
    print("Health wise: Hypothermia - seek care")
elif 35 <= temp1 < 36.1:
    print("Health wise: Slightly low")
elif 36.1 <= temp1 <= 37.2:
    print("Health wise: Normal")
elif 37.2 < temp1 < 38:
    print("Health wise: Slightly elevated")
elif 38 <= temp1 < 39:
    print("Health wise: Low-grade fever")
elif 39 <= temp1 < 40:
    print("Health wise: High fever")
else:
    print("Health wise: Very high - seek medical care")

