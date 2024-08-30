# Math Quiz Problem --->
import random
import time

operators = ["+", "-", "*"]
min_operand = 3
max_oparand = 12
total_problem = 10

def generate_problem():
    operand1 = random.randint(min_operand, max_oparand)
    operand2 = random.randint(min_operand, max_oparand)
    operator = random.choice(operators)

    expression = str(operand1) + " " + operator + " " + str(operand2)
    answer = eval(expression)
    return expression, answer

wrong =  0
input("Press Enter to Start ---> ")
print("--------------------------->")

strat_time = time.time()

for i in range(total_problem):
    expression, answer = generate_problem()
    while True:
        guess = input(f"Problem #{str(i+1)} : {expression} ---> ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - strat_time, 2)

print("---------------------------------")
print(f"Well Done! You Finished in {total_time} Seconds!")