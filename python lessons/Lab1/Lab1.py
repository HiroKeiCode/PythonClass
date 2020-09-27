#Lab 1 Input and Conditionals

#Step 1, set the password (make sure to put in lowercase
password = "pass_word12345"
cont = True

#looping
while cont:

    #Take user input
    userInput = input("welcome to password check please press N to exit \n Please enter the password: \n")

    if userInput == 'N':
        exit()

    #set all userinputs to lowecase (uppercase works too)
    userInput = userInput.lower()

    #Check the input to make sure it is valid (extra)
    for x in userInput:
        if  97 <= ord(x) <= 122 or 48 <= ord(x) <= 57 or ord(x) == 95:
            continue
        else:
            print("invalid input")
            exit()

    #check to see if valid input
    if userInput == password:
            print("correct input")
            exit()
    else:
        print("incorrect input")
