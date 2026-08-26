user_mass = float(input("What is your mass? "))
print ("Your mass: ", user_mass)
user_choice =input("what would you like kilo(K),Newtons(N)?" ).upper()

if "K":
    print (user_mass/1000.0)
elif "N":
    print (user_mass*9.81)
