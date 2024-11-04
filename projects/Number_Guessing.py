
# Number guessing game  

from random import randint as r

def game():
    try:
        num_to_be_guessed = r(1,2)   # generates a random number between 1 and 2 

        score = 0 

        while True :

            guess = input("Enter your guess 1 or 2  or type 'exit' to quit : ")   #ask the user for the guess OR IF THEY WANT TO QUIT

            if guess.lower() == "exit":
                print(f"Game ended your score is : {score}")
                break
            if guess.isdigit() and int(guess) in [1,2]:
                guess = int(guess)

                if guess == num_to_be_guessed :

                    num_to_be_guessed = r(1,2)      # if the number is guessed correctly regenrates a new number
                    print("you guessed right . guess again")
                    score+=1  
                
                else:                       # if guess is wrong game ends and tells user thier score
                    print("you lose ")
                    print(f"your score is : {score}")
                    break
            else:
                print("Invalid input. Please enter 1 or 2.")

           # if something else then number in inputed tells user to enter a valid number
    except Exception :
        print("please enter a valid number")


game()
