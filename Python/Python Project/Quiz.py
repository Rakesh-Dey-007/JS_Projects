game = input("Do you want to play game (yes/no) : ")

if game.lower() != "yes":
    print("Exiting program ...")
    quit()


print("\nOk! Let's play the game :) ")
point = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct answer! You earn 1 point.\n")
    point += 1
else:
    print("Incorrect answer. The correct answer is Central Processing Unit.\n")


answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct answer! You earn 1 point.\n")
    point += 1
else:
    print("Incorrect answer. The correct answer is Graphics Processing Unit.\n")


answer = input("What does PSU stands for? ")
if answer.lower() == "power supply unit":
    print("Correct answer! You earn 1 point.\n")
    point += 1
else:
    print("Incorrect answer. The correct answer is Power Supply Unit.\n")


answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct answer! You earn 1 point.\n")
    point += 1
else:
    print("Incorrect answer. The correct answer is Random Access Memory.\n")


print("You have earned " + str(point) + " points.")
print("You have earned " + str((point/4)*100) + "%.")