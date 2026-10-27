def onboard_passengers(bookings):
    name ="gentle man"
    counter =1
    while counter <= bookings :
        print(f"Passenger {counter} on board,",name)
        counter +=1

onboard_passengers(50)

for x in range(50,101):
    name ="lady"
    print(f'Passenger {x} on board,its a {name}')