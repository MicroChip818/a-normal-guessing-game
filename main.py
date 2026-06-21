import time
import random

def odd_or_even(number): # Hints whether the number is odd or even
    if number % 2 == 0: # Expression determining if a number is even
        return "the correct number is even. basic ahh hint i know i know"
    else:
        return "the correct number is odd. basic ahh hint i know i know"

def multiple_or_prime(number): # Hints whether the number is a multiple of a random number from 3-10 or if it is prime
    factors = []
    for i in range(3, 11): # Includes factors from 3-10
        if number % i == 0:
            factors.append(i)
    if factors:
        return f"the correct number is a multiple of {factors[random.randint(0, len(factors) - 1)]}. now we're talkin"
    elif number % 2 == 0: # Acts as the odd_or_even function if the number is only divisible by 2
        return "the correct number is even. basic ahh hint i know i know"
    else:
        return "the correct number is prime. now we're talkin"

def sum_or_difference(number): # Hints the sum or absolute value difference of the digits unless the number is less than 10
    if number < 10: # Sum or difference requires 2 digits
        return "the correct number is less than 10. ggs you win"
    elif number == 100 or number == 1 or number == 10: # All have a sum of 1
        return "the digits in the correct number add up to 1. ggs you win"
    else:
        number = str(number) # Convert to a string to allow indexing and re-converting to separate integer digits
        digit_one = int(number[0])
        digit_two = int(number[1])
        bank = ["sum", "difference"]
        action = bank[random.randint(0, 1)]
        if action == "sum":
            return f"the sum of digits in the correct number equals {digit_one + digit_two}. good luck"
        else:
            return f"the difference between digits in the correct number equals {abs(digit_one - digit_two)}. good luck"

def hints(correct_number, num_hints): # Activates an optional hint; hints are limited based on difficulty
    hint_usage = input(f"here is a free hint because im nice! type 'yes' to accept, type 'no' to reject. you have {num_hints} hints remaining: ")
    hint_bank = [odd_or_even(correct_number), multiple_or_prime(correct_number), sum_or_difference(correct_number)]
    if hint_usage == "yes":
        hint = hint_bank[random.randint(0, 2)] # Chooses a random hint from the hint bank if a hint is used
        return hint
    else:
        return None

def guess(maximum_guesses, num_hints=0): # The main function of the guessing game
    correct_number = random.randint(1, 100)
    guessed_number = -1 # Placeholder value
    guesses = 0
    while guessed_number != correct_number: # Loop exits once the correct number is guessed
        is_digit = False # Initializes variables for the input validation loop
        is_valid = False
        if guesses > 0 and num_hints > 0: # No using a hint on the first guess
            hint_stored = []
            hint_used = hints(correct_number, num_hints)
            while hint_used in hint_stored and hint_used is not None: # Ensures that a duplicate hint is not used
                hint_used = hints(correct_number, num_hints)
            hint_stored.append(hint_used)
            if hint_used is not None:
                print(hint_used)
                num_hints -= 1
            else:
                pass
        while not is_digit or not is_valid: # Input validation loop; ensures the input is an integer and is in the correct range
            guessed_number = input("guess a number between 1 and 100: ")
            if not guessed_number.isdigit(): # This line ensures the input is an integer
                print("PLEASE enter a number. don't mess up")
            else:
                is_digit = True
                guessed_number = int(guessed_number)
                if guessed_number < 1 or guessed_number > 100: # This line ensures the number is in the correct range
                    print("PLEASE enter a valid value between 1 and 100. don't mess up")
                else:
                    is_valid = True
        guesses += 1
        if guesses >= maximum_guesses:
            break # Alternatively, the loop breaks if all guesses are exhausted
        if guessed_number < correct_number:
            print(f"your number is too low. guess higher. also you have {maximum_guesses - guesses} guesses remaining")
        elif guessed_number > correct_number:
            print(f"your number is too high. guess lower. also you have {maximum_guesses - guesses} guesses remaining")
    if guessed_number != correct_number:
        print(f"unfortunately after {guesses} guesses, you failed. the correct number was {correct_number}")
        return -1, None # Returns a tuple used in a data conversion later
    else:
        print(f"good job, you win after {guesses} guesses")
        return 1, guesses

def view_statistics(**kwargs): # Prints each statistics category and its value
    for k, v in kwargs.items():
        if "_" in k: # Underscores are necessary in dictionary keys, but the printed form will consist of spaces
            k = k.replace("_", " ")
        print(f"{k}: {v}")

def append_statistics(data, wins, losses, least_guesses):
    if data[0] == 1: # If the first value in the guess() returned tuple is 1, a win is added with the number of guesses
        wins += 1
        if least_guesses is None:
            least_guesses = data[1]
        elif data[1] < least_guesses:
            least_guesses = data[1]
        else:
            pass
    else: # If the first value in the guess() returned tuple is -1, a loss is added
        losses += 1
    win_rate = round(100 * wins / (wins + losses), 1) # Percentage of games won per difficulty
    win_rate = f"{win_rate}%"
    return wins, losses, least_guesses, win_rate # Tuple of data values used for statistic variables

print("welcome to a normal guessing game i guess") # Game introduction; these introductory lines display only once
time.sleep(1) # Time between messages; 1 second
print("uhh your goal is to guess a number between 1 and 100 in as few tries as possible")
time.sleep(1)
print("there are three difficulties:\neasy (7 guesses)\nmedium (5 guesses + 1 max hint)\nhard (3 guesses + 2 max hints)")

difficulty = None # Every variable before the forever loop is initialized with 0 or None based on the context
easy_least_guesses = None
medium_least_guesses = None
hard_least_guesses = None
easy_wins = 0
easy_losses = 0
easy_win_rate = None
medium_wins = 0
medium_losses = 0
medium_win_rate = None
hard_wins = 0
hard_losses = 0
hard_win_rate = None
game_started = False
mode = None
viewed_difficulty = None

while True: # Infinite loop to keep the game going
    if game_started: # Mode switcher only works after playing the game once
        while mode != "a" and mode != "b" and mode != "c":
            mode = input("pick a valid option\nplay again ('a')\nview your statistics ('b')\nend the game ('c'): ")
            if mode != "a" and mode != "b" and mode != "c":
                print("PLEASE enter a valid option. don't mess up")
        if mode == "a":
            pass # Continues to the next game
        elif mode == "b":
            while viewed_difficulty != "easy" and viewed_difficulty != "medium" and viewed_difficulty != "hard" and viewed_difficulty != "overall":
                viewed_difficulty = input("pick a difficulty to view your statistics ('easy', 'medium', 'hard', 'overall'): ") # Allows for displaying statistics of a specific difficulty or all difficulties
                if viewed_difficulty != "easy" and viewed_difficulty != "medium" and viewed_difficulty != "hard" and viewed_difficulty != "overall":
                    print("INPUT A VALID DIFFICULTY TO VIEW AGAIN")
            if viewed_difficulty == "easy" or viewed_difficulty == "overall":
                print("easy statistics")
                easy_statistics = {"Wins": easy_wins, # Statistics based on difficulty; values are from the append_statistics() function
                    "Losses": easy_losses,
                    "Win_Percentage": easy_win_rate,
                    "Least_Guesses": easy_least_guesses}
                view_statistics(**easy_statistics) # Unpacks each key:value pair so each pair is accordingly printed
            if viewed_difficulty == "medium" or viewed_difficulty == "overall":
                print("medium statistics")
                medium_statistics = {"Wins": medium_wins,
                    "Losses": medium_losses,
                    "Win_Percentage": medium_win_rate,
                    "Least_Guesses": medium_least_guesses}
                view_statistics(**medium_statistics)
            if viewed_difficulty == "hard" or viewed_difficulty == "overall":
                print("hard statistics")
                hard_statistics = {"Wins": hard_wins,
                    "Losses": hard_losses,
                    "Win_Percentage": hard_win_rate,
                    "Least_Guesses": hard_least_guesses}
                view_statistics(**hard_statistics)
        elif mode == "c":
            exit("thanks for playing. now get out of here and be productive or something") # Exit message

    while difficulty != "easy" and difficulty != "medium" and difficulty != "hard":
        difficulty = input("choose your difficulty (type 'easy', 'medium', or 'hard'): ") # A valid difficulty must be chosen
        if difficulty != "easy" and difficulty != "medium" and difficulty != "hard":
            print("PLEASE enter a valid difficulty. don't mess up")
    if difficulty == "easy":
        easy_round_data = guess(7) # up to 7 guesses, no hints
        easy_data = append_statistics(easy_round_data, easy_wins, easy_losses, easy_least_guesses) # Data tuple per difficulty
        easy_wins = easy_data[0] # Tuple indexing since append_statistics returns a tuple
        easy_losses = easy_data[1]
        easy_least_guesses = easy_data[2]
        easy_win_rate = easy_data[3]
    elif difficulty == "medium":
        medium_round_data = guess(5, 1) # up to 5 guesses, up to 1 hint
        medium_data = append_statistics(medium_round_data, medium_wins, medium_losses, medium_least_guesses)
        medium_wins = medium_data[0]
        medium_losses = medium_data[1]
        medium_least_guesses = medium_data[2]
        medium_win_rate = medium_data[3]
    else:
        hard_round_data = guess(3, 2) # up to 3 guesses, up to 2 hints (THERE ARE MORE HINTS TO COMPENSATE FOR FEWER MAXIMUM GUESSES, SINCE THEY MAKE THE GAME EXPONENTIALLY HARDER)
        hard_data = append_statistics(hard_round_data, hard_wins, hard_losses, hard_least_guesses)
        hard_wins = hard_data[0]
        hard_losses = hard_data[1]
        hard_least_guesses = hard_data[2]
        hard_win_rate = hard_data[3]
    game_started = True # Allows the mode switcher to be used past this point
    difficulty = None # The last 3 lines reset mode switcher and difficulty values
    mode = None
    viewed_difficulty = None