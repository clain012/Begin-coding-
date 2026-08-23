Temperature = float(input("Your temperature? "))
unit = input("To Kelvin(K) or Fahrenheit(F)? ").upper()
if unit == "K":
    converter = Temperature + 273.15
    print ("Temperature in Kelvin: ",converter)
elif unit == "F":
    converter = Temperature*1.8 +32
    print ("Temperature in Fahrenheit: " ,converter)
else:
    print ("Enter either K or F")
