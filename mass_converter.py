while True:
    try :
        user_mass = float(input("What is your mass?  "))
        break
    except ValueError:
        print ("Not valid,enter digits solely..." )
print ("Your mass: ",user_mass)

while True:
    user_choice =input("what would you like kilo(K),Newtons(N)?  ").strip().upper()
    if user_choice in ("K","N"):
        break
    print ("Invalid response ,enter K or N ")

if user_choice == "K":
    print (user_mass/1000.0)
elif user_choice == "N"
    print (user_mas*9.81)
