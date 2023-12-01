# rock paper siccors
import random
import sys
print("Welcome to rock paper sciccors! \n")
choice = int(input("Do you want to play 0 for rock, 1 for Scissors, or 2 for Paper? "))

if choice > 2 or choice < 0:
    print("You lost! You cant type a number > than 2 or < than 0!!")
    sys.exit()

cp_choices = random.randint(0, 2)
möglichkeiten = ["Rock", "Sciccors", "Paper"]

if choice == cp_choices:
    print(f"Oh no you both played {möglichkeiten[choice]}, this is a stalemate")
elif cp_choices >= choice -1:
      print(f"Oh sadly you lost! The computer player {möglichkeiten[cp_choices]} and you played {möglichkeiten[choice]}")

else:
    print(f"Congrats you won!! The ccomputer played {möglichkeiten[cp_choices]} and you played {möglichkeiten[choice]}")

print(cp_choices)