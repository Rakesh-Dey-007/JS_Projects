from time import time
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except IndexError:
            error += 1
    return error

def speed_time(time_s, time_e, user_input):
    time_delay = time_e - time_s
    num_words = len(user_input.split())
    speed = num_words / time_delay * 60  # Convert to wpm
    return round(speed)

test = ["Hello i am Rakesh", "The quick brown fox jumps over the lazy dog.", "Follow and Like"]
test1 = r.choice(test)
print(" -------> Typing Speed <-------")
print()
print(test1)
print()
time_1 = time()
test_input = input("Enter : ")
time_2 = time()

print("Speed : ", speed_time(time_1, time_2, test_input), "wpm")
print("Error : ", mistake(test1, test_input))