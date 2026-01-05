# MadDogSlayer4
# No Packages Need To Be Installed

import random
import time
import copy

# Definitions -----
def selectMode():
    prGreen(r"""
     ____          __  __      _   _     
    |  _ \  ___   |  \/  | ___| |_| |__  
    | | | |/ _ \  | |\/| |/ _ \ __| '_ \ 
    | |_| | (_) | | |  | |  __/ |_| | | |
    |____/ \___/  |_|  |_|\___|\__|_| |_|
    
        Press Control-C To Exit
            """)
    while True:
        difficulty = input("Select difficulty: \n 1. Easy \n 2. Medium \n 3. Hard \n").lower().strip()
        print("\n")
        if difficulty in ["1", "2", "3", "easy", "medium", "hard"]:
            break
        else:
            prRed("\n" * 100+"Please Select Right difficulty")
    while True:
        mode = input("Select mode: \n 1. Multiplication \n 2. Division \n 3. Addition \n 4. Subtraction \n 5. OhShit \n").lower().strip()

        if mode == "multiplication" or mode == "1":
            mode = ["*"]
            if difficulty == "easy" or difficulty == "1":
                low = 1
                high = 10
            if difficulty == "medium" or difficulty == "2":
                low = 2
                high = 100
            if difficulty == "hard" or difficulty == "3":
                low = 9
                high = 500
            break
        if mode == "division" or mode == "2":
            mode = ["/"]
            if difficulty == "easy" or difficulty == "1":
                low = 2
                high = 33
            if difficulty == "medium" or difficulty == "2":
                low = 2
                high = 100
            if difficulty == "hard" or difficulty == "3":
                low = 9
                high = 1000
            break
        if mode == "addition" or mode == "3":
            mode = ["+"]
            if difficulty == "easy" or difficulty == "1":
                low = 1
                high = 10
            if difficulty == "medium" or difficulty == "2":
                low = 9
                high = 100
            if difficulty == "hard" or difficulty == "3":
                low = 19
                high = 750
            break
        if mode == "subtraction" or mode == "4":
            mode = ["-"]
            if difficulty == "easy" or difficulty == "1":
                low = 1
                high = 10
            if difficulty == "medium" or difficulty == "2":
                low = 9
                high = 100
            if difficulty == "hard" or difficulty == "3":
                low = 19
                high = 750
            break
        if mode == "ohshit" or mode == "5":
            if difficulty == "easy" or difficulty == "1":
                low = 1
                high = 20
                mode = ["-", "+"]
            if difficulty == "medium" or difficulty == "2":
                low = 9
                high = 100
                mode = ["-", "+", "*"]
            if difficulty == "hard" or difficulty == "3":
                low = 19
                high = 250
                mode = ["-", "+", "*", "/"]
            break
        else:
            prRed("\n" * 100 + "Please Select Correct Mode!")
    
    # Choose rounds
    while True:
        try:
            rounds = int(input("Select number of rounds (10, 20, 30, ect)\n").strip())
            print("\n")
            break
        except ValueError:
            prRed("\n" * 100+"Please Select A Number")
    return low, high, mode, rounds

def guessMath(low, high, ops, rounds):
    """Returns list showing correct answers and time it took to do all the math"""
    correct = []
    initialTime = time.perf_counter()
    for round in range(rounds):

        while True:
            nums = []
            for i in range(len(ops)+1):
                nums.append(random.randint(low, high))
            answer = doMath(nums, ops)

            # Check if division works
            if ops == "/" and answer % 1 == 0:
                break
            elif ops != "/":
                break
        while True:
            print(f"{round+1}/{rounds} (q) to exit")
            
            printMath(nums, ops)

            try:
                guess = input()
                if int(guess) == answer:
                    correct.append(True)
                    prGreen("\n" * 100 + "Correct!")
                else:
                    prRed(f"\n" * 100 + "Incorrect. It was " + str(answer))
                    correct.append(False)
                break
            except ValueError:
                if str(guess).lower() == "q":
                    return correct, time.perf_counter() - initialTime
                prRed("\n" * 100 + "Incorrect input. Please enter a number!")

    return correct, time.perf_counter() - initialTime

def doMath(numss, opss):
    """Takes in numbers and adds them with the operators in the correct order of PEMDAS
    Returns none if wrong amount of operators or numbers are inputed"""
    nums = copy.deepcopy(numss)
    ops = copy.deepcopy(opss)

    # Do Math
    if len(ops) != len(nums) - 1:
        print("Wrong ammount of operators or numbers inputed")
        return None
    while len(nums) > 1:
        count = 0
        popThese = []
        for op in ops:

            if op == '^':
                nums[count+1] = nums[count] ** nums[count+1]
                popThese.append(count)
                nums.pop(count)
                count -= 1

            if op == '*' and "^" not in ops:
                nums[count+1] = nums[count] * nums[count+1]
                popThese.append(count)
                nums.pop(count)
                count -= 1

            elif op == '/' and "^" not in ops and "*" not in ops:
                nums[count+1] = nums[count] / nums[count+1]
                popThese.append(count)
                nums.pop(count)
                count -= 1
                
            elif op == '+' and "^" not in ops and "*" not in ops and "/" not in ops:
                nums[count+1] = nums[count] + nums[count+1]
                popThese.append(count)
                nums.pop(count)
                count -= 1

            elif op == '-' and "^" not in ops and "*" not in ops and "/" not in ops and "+" not in ops:
                nums[count+1] = nums[count] - nums[count+1]
                popThese.append(count)
                nums.pop(count)
                count -= 1

            count += 1
        for popem in popThese:
            ops.pop(popem)

    return nums[-1]

def printMath(nums, ops):
    count = 0
    for op in ops: 
        print(f"{nums[count]}", end=" ")
        print(f"{op}", end=" ")
        count += 1
    print(nums[count])

def prRed(s): print("\033[91m {}\033[00m".format(s))
def prGreen(s): print("\033[92m {}\033[00m".format(s))

# Program Starts -------

while True:
    low,high,ops,rounds = selectMode()

    goAgain = "y"
    while goAgain == "y":
        print("\n" * 100)
        correct, timeTook = guessMath(low, high, ops, rounds)
        
        ## Checks input
        while True:
            try:
                goAgain = input(f"{sum(correct)}/{len(correct)} correct! \nTook {timeTook:.2f} seconds\n"
            "Want to go again (y/n)? \n").lower().strip()
                if goAgain in ["y", "n", "q"]:
                    break
                else:
                    prRed("Input must be y or n.")
            except ValueError:
                prRed("Invalid input. Please enter a (y/n)")
