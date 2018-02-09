
def player_1():
    global numbs1,score1,lis1,continuety
    while continuety:
        print("Welcome: {} ".format(numbs1))
        index1 = int(input("Player#1 – score {}:".format(score1)))
        index2 = int(input("Player#1 – score {}:".format(score1)))

        if lis1[index1] == "*" and lis1[index2] == "*" or index1 == index2:
            print("Invalid both position")

        elif lis1[index1] == lis1[index2]:

            score1 = score1 + 1
            print(lis1[index1], lis1[index2])

            numbs1.remove(index1)
            numbs1.remove(index2)
            lis1 = list(lis1)
            lis1[index1] = "*"
            lis1[index2] = "*"
            lis1 = "".join(lis1)
            print(lis1)
        elif lis1[index1] == "*":
            print("Invalid first position ")

        elif lis1[index2] == "*":
            print("Invalid second position")

        else:
            print(lis1[index1], lis1[index2])
            numbs1.remove(index1)
            numbs1.remove(index2)
            lis1 = list(lis1)
            lis1[index1] = "*"
            lis1[index2] = "*"
            lis1 = "".join(lis1)
            print(lis1)
        continuety = False


def player_2():
    global numbs2,score2,lis2,continuety
    while continuety :
        print("Welcome: {} ".format(numbs2))
        index3 = int(input("Player#2 – score {}:".format(score2)))
        index4 = int(input("Player#2 – score {}:".format(score2)))
        if lis2[index3] == "*" and lis2[index4] == "*" or index3 == index4:
            print("Invalid both position")

        elif lis2[index3] == lis2[index4]:

            score2 = score2 + 1
            print(lis2[index3], lis2[index4])

            numbs2.remove(index3)
            numbs2.remove(index4)
            lis2 = list(lis2)
            lis2[index3] = "*"
            lis2[index4] = "*"
            lis2 = "".join(lis2)
            print(lis2)
        elif lis2[index3] == "*":
            print("Invalid first position ")

        elif lis2[index4] == "*":
            print("Invalid second position")

        else:
            print(lis2[index3], lis2[index4])
            numbs2.remove(index3)
            numbs2.remove(index4)
            lis2 = list(lis2)
            lis2[index3] = "*"
            lis2[index4] = "*"
            lis2 = "".join(lis2)
            print(lis2)


lis1 = "FZXVLGHASDZLXVADHFGS"
score1 = 0
numbs1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
#Player 2 status########################
lis2 = "ABDCHFGZLKGACDFLZBHK"
score2 = 0
numbs2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
continuety = True

while True :
    if numbs1 == [] and numbs2 == [] :
        if score1 > score2 :
            print("__________________________________Player 1 is Won_____________________________________")
            break
        elif score2 > score1:
            print("__________________________________Player 2 is Won_____________________________________")
            break

        else:
            print("______________________________________DRAW_________________________________________")
            break

    print("Welcome: {} ".format(numbs1))
    index1=int(input("Player#1 – score {}:".format(score1)))
    index2=int(input("Player#1 – score {}:".format(score1)))

    if lis1[index1] == "*" and lis1[index2] == "*" or index1 == index2 :
        print("Invalid both position")
        player_1()

    elif lis1[index1] == lis1[index2]  :

        score1 = score1+1
        print(lis1[index1], lis1[index2])

        numbs1.remove(index1)
        numbs1.remove(index2)
        lis1=list(lis1)
        lis1[index1] = "*"
        lis1[index2] = "*"
        lis1 = "".join(lis1)
        print(lis1)
    elif lis1[index1] == "*" :
        print("Invalid first position ")
        player_1()

    elif lis1[index2] == "*" :
        print("Invalid second position")
        player_1()
    else:
        print(lis1[index1], lis1[index2])
        numbs1.remove(index1)
        numbs1.remove(index2)
        lis1 = list(lis1)
        lis1[index1] = "*"
        lis1[index2] = "*"
        lis1 = "".join(lis1)
        print(lis1)


##Player 2 #########################################################
    print("__________________________________Clear____________________________________")

    print("Welcome: {} ".format(numbs2))
    index3=int(input("Player#2 – score {}:".format(score2)))
    index4=int(input("Player#2 – score {}:".format(score2)))
    if lis2[index3] == "*" and lis2[index4] == "*" or index3 == index4 :
        print("Invalid both position")
        player_2()

    elif lis2[index3] == lis2[index4]  :

        score2 = score2+1
        print(lis2[index3], lis2[index4])
        numbs2.remove(index3)
        numbs2.remove(index4)
        lis2=list(lis2)
        lis2[index3] = "*"
        lis2[index4] = "*"
        lis2 = "".join(lis2)
        print(lis2)

    elif lis2[index3] == "*" :
        print("Invalid first position ")
        player_2()

    elif lis2[index4] == "*" :
        print("Invalid second position")
        player_2()


    else:
        print(lis2[index3], lis2[index4])
        numbs2.remove(index3)
        numbs2.remove(index4)
        lis2 = list(lis2)
        lis2[index3] = "*"
        lis2[index4] = "*"
        lis2 = "".join(lis2)
        print(lis2)
    print("__________________________________Clear____________________________________")
































