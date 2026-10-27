
while True:
    user_operation =input("What operation today;adding(A),subtracting(S),multiplying(M) or dividing(D): ").upper()
    if user_operation in ("A","S","M","D"):
        break
    print("Choose of;adding(A),subtracting(S),multiplying(M) or dividing(D):  ")

while True:
    try:
        first = float(input("Enter a number: "))
        break
    except ValueError:
        print('please enter number solely: ')
while True:
    try:
        second = float(input("Enter a number: "))
        break
    except ValueError:
        print('please enter number solely: ')

if user_operation == "A":
    answer=first+second
    print(f"{first}+{second} = ",answer)
elif user_operation == "S":
    answer = first -second
    print(f"{first}-{second} = ",answer)
elif user_operation =="M":
    answer =first*second
    print(f"{first}*{second} = ",answer)
else:
    answer = first/second
    print(f"{first}/{second} = ",answer)

