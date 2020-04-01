import os
import random
def tic_tac_toe():
    #main Game
    print("=========Welcome to the TIC-TAC-TOE Game============")
    player_one = input("enter player one name")
    player_two = input("enter player two name")
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def display():
        #board display
        print(board[0]+"|"+board[1]+"|"+board[2])
        print("------")
        print(board[3]+"|"+board[4]+"|"+board[5])
        print("------")
        print(board[6]+"|"+board[7]+"|"+board[8])
        print()

    def p1():
        #player one chance
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p1()
            #os.system('cls')
        else:
            board[n] = "X"
            #os.system('cls')

    def p2():
        # player two chance
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p2()
            #os.system('cls')
        else:
            board[n] = "O"
            #os.system('cls')

    def choose_number():
        # choosing number
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nThat's not on the board. Try again")
                        #os.system('cls')
                        continue
                except ValueError:
                   print("\nThat's not a number. Try again")
                   #os.system('cls')
                   continue

    def check_board():
        #combination checking and finalizing the result
        count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print(player_one +"Wins!\n")
                print("Congratulations!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print(player_two +"Wins!\n")
                print("Congratulations!\n")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
                return True
    #main fuction
    while not end:
        #os.system("clear")
        print()
        display()
        end = check_board()
        if end == True:
            break
        print(player_one+" choose where to place a cross")
        p1()
        #os.system('cls')
        print()
        #os.system("clear")
        print()
        display()
        end = check_board()
        if end == True:
            break
        print(player_two +" choose where to place a nought")
        p2()
        #os.system('cls')
        print()

    if input("Play again (y/n)\n") == "y":
        #os.system("clear")
        print()
        tic_tac_toe()

    #pc game (not yet complted)
    #def pc():
     #   n = print(random.randint(0, 5))
      #  print("pc entered "+n)
       # if board[n] == "X" or board[n] == "O":
        #    print("\nYou can't go there. Try again")
         #   p2()
          #  #os.system('cls')
        #else:
         #   board[n] = "O"
            #os.system('cls')



tic_tac_toe()