# secreat number
Secreat_number = 29

#while loop for guess the number
while True:

    # user input
    user = int(input("Guess the number between 1 to 100 ? "))

    # if conditon for match the user input
    if user == Secreat_number:
        print('congratulation You are right')
        break

    else:
        print('Try Again')