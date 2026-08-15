# # frist project
# def totalAgeInDays():
#     age_years = int(input("Enter your age in years: "))
#     age_days = age_years * 365
#     age_month = age_years * 12
#     age_hour = age_days * 24
#     print(f"""You have lived for
#     \n{age_month} month
#     \n{age_days} days
#     \n{age_hour} hours
#     """)


# totalAgeInDays()

# import random


# def guessGame():
#     print("🎲 Welcome to the Number Gussing Game")

#     numberToGuess = random.randint(1, 10)
#     conut = 0

#     while True:
#         guess = int(input("Guess a nimber between 1 to 10: "))
#         conut += 1
#         if numberToGuess > guess:
#             print("low! Try again")

#         elif numberToGuess < guess:
#             print("Hihg! Try again")

#         elif numberToGuess == guess:
#             print(f"Correct! you guessed the number in {conut} tries")
#             break


# guessGame()

# import datetime

# def pomodoro():
#     print("Welcome to the pomodoro Timer!")

#     user=input("Enter time in minutes: ")
#     print(f"Time remaining : {user}")


