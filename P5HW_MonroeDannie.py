#Dannie Monroe
#12072023
#Use functions, random numbers, and while loop

#Import the random library
import random

#This function displays Main Menu
def show_menu():
    print("Welcome To Math Quiz")
    print("Main Menu")
    print("---------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")

#This function adds two random numbers
def add():
    ran1 = random.randint(0, 10)
    ran2 = random.randint(0, 10)
    print(f"{ran1} + {ran2}")
    return (ran1 + ran2)

#This function subtracts two random numbers
def subtract():
    ran1 = random.randint(0, 10)
    ran2 = random.randint(0, 10)
    print(f"{ran1} - {ran2}")
    return (ran1 - ran2)

#This function simulates the user guessing
#while the guess is wrong keep letting them try
def guessing(guess, correct_answer):
    num_guess = 0
    while guess != correct_answer:
        num_guess += 1
        if guess > correct_answer:
            print("TOO HIGH")
            guess = int(input("Guess Again "))
        else:
            print("too low")
            guess = int(input("Guess Again "))
    #User answer is correct, the while loop breaks    
    print("YOU DID IT GREAT JOB")
    print(f"It took you {num_guess} incorrect guesses to get it right")
    
#Main Function
def main():
    show_menu()
    user_option = int(input("Please Choose One Of The Menu Options: "))
    while user_option != 3: 
        if user_option ==1:
            ran_sum = add()        #represents the correct answer
            my_guess = int(input("What is your guess? ")) #represents guess
            guessing(my_guess,ran_sum)
            print()
            show_menu()
            user_option = int(input("Please Choose One Of The Menu Options: "))
            
        if user_option == 2: 
            ran_sum = subtract()        #represents the correct answer
            my_guess = int(input("What is your guess? ")) #represents guess
            guessing(my_guess,ran_sum)
            print()
            show_menu()
            user_option = int(input("Please Choose One Of The Menu Options: "))
            
    #If user_choice == 3, the while loop breaks
    print("Thank you for playing, goodbye!")
#Call the main function
if __name__ == "__main__":
    main()
        
        
