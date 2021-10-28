import random

min_val = 1
max_val = 6
global guess
guess = 'yes'
first = int(input("Enter Number to guess: "))
second = int(input("Enter Number to guess: "))

while guess=='yes' or guess=='y':
    first_no = random.randint(1,6)
    second_no = random.randint(1,6)
    if first ==first_no and second == second_no :
         print('Guessed numbers correct')
         break
    else:
        print("Guess is wrong")

guess = input("You want to roll the dice(yes(y)/no): ")
#print("Total number of guesses",count)