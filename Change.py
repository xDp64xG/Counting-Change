#Variables for the change
Twenty = 0
Ten = 0
Five = 0
One = 0
Q = 0
D = 0
N = 0
P = 0

#Print the change using a list
Msg = [""]

#Have some loops for continous use
Bool = False
Bool2 = False
Bool3 = False

#First loop is for multiple change
while Bool2 == False:
    change = float(input("Enter your change: "))
    #If you input 0, quits program
    if change == 0:
        Bool2 = True
        break
    #Little function to subtract from the change and a specific number given
    def func(change, num):
        change = change - num
        change = round(change, 2)
        return change

    #This loop is to go through ALL the change, and then give the total
    while Bool == False:

        #If I would subtract 20, would it equal to or more than 0? If so, move forward. Same as the other ifs
        if (change - 20) >= 0:
            change = func(change, 20)
            Twenty += 1

        elif (change - 10) >= 0:
            change = func(change, 10)
            Ten += 1

        elif (change - 5) >= 0:
            change = func(change, 5)
            Five += 1

        elif (change - 1) >= 0:
            change = func(change, 1)
            One += 1

        elif (change - .25) >= 0:
            change = func(change, .25)
            Q += 1

        elif (change - .10) >= 0:
            change = func(change, .10)
            D += 1

        elif (change - .05) >= 0:
            change = func(change, .05)
            N += 1

        elif (change - .01) >= 0:
            change = func(change, .01)
            P += 1

        #After all change is counted, stop the loop by setting Bool to True
        else:
            Bool = True

    #This loop allows to show ONLY the change, and not any extras, such as (20) Twenties 1, Tens 0, etc.
    while Bool3 == False:
        if Twenty != 0:
            #2nd check to see if its singular or multiple.
            if Twenty > 1:
                Msg.append("{} Twenties".format(Twenty))
            else:
                Msg.append("{} Twenty".format(Twenty))
            Twenty = 0

        elif Ten != 0:
            if Ten > 1:
                Msg.append("{} Tens ".format(Ten))
            else:
                Msg.append("{} Ten".format(Ten))
            Ten = 0

        elif Five != 0:
            if Five > 1:
                Msg.append("{} Fives ".format(Five))
            else:
                Msg.append("{} Five".format(Five))
            Five = 0

        elif One != 0:
            if One > 1:
                Msg.append("{} Ones ".format(One))
            else:
                Msg.append("{} One".format(One))
            One = 0

        elif Q != 0:
            if Q > 1:
                Msg.append("{} Quarters ".format(Q))
            else:
                Msg.append("{} Quarter".format(Q))
            Q = 0

        elif D != 0:
            if D > 1:
                Msg.append("{} Dimes ".format(D))
            else:
                Msg.append("{} Dime".format(D))
            D = 0

        elif N != 0:
            if N > 1:
                Msg.append("{} Nickels ".format(N))
            else:
                Msg.append("{} Nickel".format(N))
            N = 0

        elif P != 0:
            if P > 1:
                Msg.append("{}Pennies ".format(P))
            else:
                Msg.append("{} Penny".format(P))
            P = 0

        #Reset the loop for continous use
        else:
            Bool3 = True
    #Print the list
    for i in Msg:
        print(i)

    #Reset the loops and message, and start again
    Msg = [""]
    Bool3 = False
    Bool = False

print("End.")