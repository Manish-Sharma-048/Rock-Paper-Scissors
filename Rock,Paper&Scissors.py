#Rock, Paper and Scissors
import random
def ran_num():
    ran = random.randrange(0, 3)
    return ran

r = 0
p = 1
s = 2
comp = 0
player = 0
tie = 0
def rps():
    global comp, player, tie
    print("\t------Its time to play Rock, Papers and Scissors------\n")
    print("Please enter your choice.\n0 for Rock\n1 for Paper\n2 for Scissors\n")
    choice =int(input("Your choice is: "))
    c_choice = ran_num()
    if choice == c_choice:
        print("Oh! It's a tie.")
        tie = tie + 1
        play_again()
    elif choice == r:
        if choice == r and c_choice == 1:
            print("Computer wins")
            comp = comp + 1
            play_again()
        else:
            print("Player wins")
            player = player + 1
            play_again()
    elif choice == p:
        if choice == p and c_choice == 2:
            print("Computer wins")
            comp = comp + 1
            play_again()
        else:
            print("Player wins")
            player = player + 1
            play_again()
    elif choice == s:
        if choice == s and c_choice == 0:
            print("Computer wins")
            comp = comp + 1
            play_again()
        else:
            print("Player wins")
            player = player + 1
            play_again()
    else:
        print("Invalid value")
        rps()
        
def play_again():
    print("\n\n\tWould you like to play again: ")
    p_again = input("\n\nEnter\nYes --> to play again\nNo --> to exit\nScore --> to see the score\nYour choice: ")
    print("\n")
    p_again = p_again.upper()
    if p_again == "YES":
        rps()
    elif p_again == "NO":
        exit()
    elif p_again == "SCORE":
        print("Computer won: ", comp)
        print('Player won: ', player)
        print("Games tied: ", tie)
    else:
        print("Invalid value")
        play_again()

rps()
play_again()
