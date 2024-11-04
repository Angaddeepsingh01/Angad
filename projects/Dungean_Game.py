



# dungean game

import random
from random import randint as r
import time


def dungean():

        ask_player = input("Would you like to enter the\n Dungean of Dreams. \nYes or No : ").capitalize()

        while True:
            if ask_player == "Yes":
                
                time.sleep(1)

                print("You have entered the Dungean.")

                time.sleep(0.5)
               
                door = input("Choose a door to enter \n  WEALTH     FAME    Power\n->").capitalize()
                print(f"You will be entering {door} door")

                if door == "Wealth":
                    wealth_path()

                elif door == "Fame":
                    fame_path()

                elif door == "Power":
                    power_path()


                else:

                    print("This doesn't exist\nyou left")
                    break


            elif ask_player == "No":
                print("You left.")
                break

            else:
                print("Invalid input.")
                break







def power_path():
   choice =  input("What type of power would you like to have. Political power or Raw strength \n Political or Strength -> ").lower() 

   if choice == "political":
        political_path() 
   elif choice =="strength":
         strength_path()


def political_path():
    print("You have chosen the Political path.")
    influence = r(100, 500)
    print(f"Your initial influence: {influence}")
    time.sleep(1)

    # Define randomized political scenarios
    scenarios = [
        ("Election Campaign", "An election is coming up. Will you run a campaign or save your resources?"),
        ("Debate Challenge", "A rival challenges you to a public debate. Do you accept?"),
        ("Controversial Policy", "You are pressured to support a controversial policy. Will you back it?"),
        ("Corruption Scandal", "A scandal surfaces about one of your close associates. How will you handle it?"),
        ("Public Speech", "You have the opportunity to give a major speech. Will you address sensitive issues?"),
        ("Ally Support", "A powerful ally requests your public support. Will you align with them?"),
        ("Press Conference", "A sudden crisis demands a press conference. Will you address it head-on?")
    ]

    random.shuffle(scenarios)  # Randomize the order of scenarios

    continue_playing = "yes"
    while continue_playing == "yes":
        for scenario, description in scenarios:
            print(f"\nScenario: {description}")
            influence = perform_action_pol(influence, scenario)  # Perform action based on scenario
            
            if influence <= 0:
                print("Your influence has dwindled to zero. Your political career is over! GAME OVER!")
                return  # End the function if influence drops to zero
            
            # Prompt user to continue after each scenario
            continue_playing = input("\nDo you want to continue the Political path? (Yes/No) -> ").lower()
            if continue_playing != "yes":
                print(f"Final influence: {influence}. Thanks for playing!")
                return  # Exit the game if the user says "No"

def perform_action_pol(influence, action_type):
    # Prompt for each scenario
    prompts = {
        "Election Campaign": "Do you choose to run an expensive campaign? (Run/Save Resources) -> ",
        "Debate Challenge": "Do you accept the debate challenge? (Accept/Decline) -> ",
        "Controversial Policy": "Do you back the controversial policy? (Support/Oppose) -> ",
        "Corruption Scandal": "Do you defend your associate or cut ties? (Defend/Cut Ties) -> ",
        "Public Speech": "Do you address sensitive issues in your speech? (Address/Play Safe) -> ",
        "Ally Support": "Do you publicly support your ally? (Support/Neutral) -> ",
        "Press Conference": "Do you address the crisis head-on or avoid questions? (Address/Avoid) -> "
    }

    # Define actions and possible results
    actions = {
        "run": lambda: random.choice(["success", "fail"]),
        "accept": lambda: random.choice(["success", "fail"]),
        "support": lambda: random.choice(["success", "fail"]),
        "defend": lambda: random.choice(["success", "fail"]),
        "address": lambda: random.choice(["success", "fail"]),
        "cut ties": lambda: random.choice(["success", "fail"]),
        "oppose": lambda: "neutral",
        "decline": lambda: "neutral",
        "play safe": lambda: "neutral",
        "neutral": lambda: "neutral",
        "avoid": lambda: "neutral",
        "save resources": lambda: "neutral"
    }

    response = input(prompts.get(action_type, "Invalid scenario")).lower()
    result = actions.get(response, lambda: "invalid")()

    if result == "success":
        influence += 50
        print(f"Success! Your influence increased to {influence}.")
    elif result == "fail":
        influence -= 50
        print(f"Failure! Your influence decreased to {influence}.")
    elif result == "neutral":
        print("You played it safe. Influence remains the same.")
    else:
        print("Invalid choice, try again.")
    
    return influence






def strength_path():
    print("You have chosen the Strength path.")
    strength = r(100,500)
    print(f"Your strngth : {strength}")
    time.sleep(1)

    scenarios = [
        ("Mountain Climb Challenge", "You've been challenged to climb the most treacherous mountain in the region."),
        ("Arena Fight", "A legendary warrior challenges you to a fight in the arena."),
        ("Rescue Mission", "A village is under attack, and they need a hero to defend them."),
        ("Test of Endurance", "Prove your endurance by surviving a week in the wilderness with limited supplies."),
        ("Dragon Hunt", "A dragon has been terrorizing the countryside. Will you hunt it?"),
        ("Strength Training", "Dedicate time to intense training to build your strength."),
        ("Defend the Castle", "Enemies are attacking your castle, and you must lead the defense.")
    ]

    random.shuffle(scenarios)  # Randomize the order of scenarios


    # checks if the player is  still playing and has not typed antthing other then yes

    continue_playing = "yes"
    while continue_playing == "yes":
        for scenario, description in scenarios:
            print(f"\nScenario: {description}")
            strength = perform_action(strength, scenario)  # Perform action based on scenario
            
            if strength <= 0:
                print("Your career is over! GAME OVER!")
                break # End the function if strength drops to zero
            
            # Prompt user to continue after each scenario
            continue_playing = input("\nDo you want to continue the Gangster path? (Yes/No) -> ").lower()
            if continue_playing != "yes":
                print(f"Final strength: {strength}. Thanks for playing!")
                break # Exit the game if the user says "No"





def perform_action_str(strength, action_type):  # **Merged perform_action for strength_path function**

    # Takes input from user 
    prompts = {
        "Mountain Climb Challenge": "Do you attempt the climb? (Climb/Decline) -> ",
        "Arena Fight": "Do you accept the fight? (Fight/Withdraw) -> ",
        "Rescue Mission": "Do you step in to rescue the village? (Rescue/Stay Back) -> ",
        "Test of Endurance": "Do you take the endurance test? (Test/Decline) -> ",
        "Dragon Hunt": "Do you choose to hunt the dragon? (Hunt/Retreat) -> ",
        "Strength Training": "Do you engage in intense training? (Train/Rest) -> ",
        "Defend the Castle": "Do you lead the castle defense? (Defend/Flee) -> "
    }

    # Define actions and possible results
    actions = {
        "climb": lambda: random.choice(["success", "fail"]),
        "fight": lambda: random.choice(["success", "fail"]),
        "rescue": lambda: random.choice(["success", "fail"]),
        "test": lambda: random.choice(["success", "fail"]),
        "hunt": lambda: random.choice(["success", "fail"]),
        "train": lambda: random.choice(["success", "fail"]),
        "defend": lambda: random.choice(["success", "fail"]),
        "decline": lambda: "neutral",
        "withdraw": lambda: "neutral",
        "stay back": lambda: "neutral",
        "retreat": lambda: "neutral",
        "rest": lambda: "neutral",
        "flee": lambda: "neutral"
    }


    response = input(prompts[action_type]).lower()  # **Use action_type to fetch prompt**
    result = actions.get(response, lambda: "invalid")()

    if result == "success":
        strength += 50
        print(f"Success! Your strength increased to {strength}.")
    elif result == "fail":
        strength -= 50
        print(f"Failure! Your strength decreased to {strength}.")
    elif result == "neutral":
        print("You played it safe. strength remains the same.")
    else:
        print("Invalid choice, try again.")
    
    return strength



def fame_path():

    fame  = r(100,500)
    print(f"your Fame :{fame} ")

    
    choice  = input("Would you like to be a Celebrity or be a Gangster of underworld. \n (Celebrity or Gangster) -> ").lower()

    if choice == "gangster":
        gangster(fame)
    elif choice == "celebrity":
        celebrity(fame)



def gangster(fame):
    print("You have chosen the Gangster path.")
    time.sleep(1)

    # the scenarios 

    scenarios = {
        "heist": "You're tasked with a dangerous heist to boost your fame.",
        "hitman": "A contract to take out a high-profile target has come your way.",
        "police": "The police are after you! How will you escape?"
    }
     
    # checks if the player is  still playing and has not typed antthing other then yes

    continue_playing = "yes"
    while continue_playing == "yes":
        for scenario, description in scenarios.items():
            print(f"\nScenario: {description}")
            fame = perform_action(fame, scenario)  # Perform action based on scenario
            
            if fame <= 0:
                print("Your career is over! GAME OVER!")
                break # End the function if fame drops to zero
            
            # Prompt user to continue after each scenario
            continue_playing = input("\nDo you want to continue the Gangster path? (Yes/No) -> ").lower()
            if continue_playing != "yes":
                print(f"Final Fame: {fame}. Thanks for playing!")
                break # Exit the game if the user says "No"


def celebrity(fame):
    print("You have chosen the Celebrity path.")
    time.sleep(1)

    
    # The scenarios 

    # The scenarios as a list to enable randomization
    scenarios = [
        ("movie", "You are given a movie to star in."),
        ("collab", "You have the chance to collaborate with another celebrity."),
        ("scandal", "You've been caught in a scandal.")
    ]

    # Shuffle the scenarios for random order
    random.shuffle(scenarios)

    # checks if the player is  still playing and has not typed antthing other then yes

    continue_playing = "yes"
    while continue_playing == "yes":
        for scenario, description in scenarios:
            print(f"\nScenario: {description}")
            fame = perform_action(fame, scenario)  # Perform action based on scenario
            
            if fame <= 0:
                print("Your career is over! GAME OVER!")
                break  # End the function if fame drops to zero
            
            # Prompt user to continue after each scenario
            continue_playing = input("\nDo you want to continue the celebrity path? (Yes/No) -> ").lower()
            if continue_playing != "yes": 
                print("Calculating your fame.....")
                time.sleep(1.5)
                if fame<660:
                        print(f"You are not famous enough.\nPeople forgot you.\nYou died misreably!")
                else:
                    print(f"Your Fame: {fame}.\n YOU WON !!!\nThanks for playing!")

                break  # Exit the game if the user says "No"



def perform_action(fame, action_type):  # **Merged perform_action function**

    # Takes input from user 
    prompts = {
        "heist": "Do you take on the risky heist? (Yes/No) -> ",
        "hitman": "Do you accept the hit? (Yes/No) -> ",
        "police": "Do you speed off in a stolen car or lay low? (Drive/Lay Low) -> ",
        "movie": "Do you want to take the movie role? (Yes/No) -> ",
        "collab": "Do you accept the collaboration? (Yes/No) -> ",
        "scandal": "Do you stay silent or apologize? (Stay Silent/Apologize) -> "
    }

    # Checks the input from the user is in actions and perform the action

    actions = {
        "yes": lambda: random.choice(["success", "fail"]),
        "drive": lambda: random.choice(["success", "fail"]),
        "stay silent": lambda: random.choice(["success", "fail"]),
        "apologize": lambda: random.choice(["success", "fail"]),
        "lay low": lambda: "neutral",
        "no": lambda: "neutral"
    }


    response = input(prompts[action_type]).lower()  # **Use action_type to fetch prompt**
    result = actions.get(response, lambda: "invalid")()

    if result == "success":
        fame += 50
        print(f"Success! Your fame increased to {fame}.")
    elif result == "fail":
        fame -= 50
        print(f"Failure! Your fame decreased to {fame}.")
    elif result == "neutral":
        print("You played it safe. Fame remains the same.")
    else:
        print("Invalid choice, try again.")
    
    return fame


def wealth_path() :
    
    
      wealth = r(1,1000)
      print(f"Your wealth is : {wealth}")
      
      choice  = input("Would you like to increase your wealth or live life of luxury. \n (increase or luxury) -> ").lower()

      if choice == "increase":
        increase(wealth)
      elif choice == "luxury":
        luxury(wealth)



def increase(wealth):
         while True:

            print("To quit incresing wealth Type exit")

            stocks = ["snake.co" ,"monsternail.inc"  ,  "zombiebrains.big"]
            stock = input(f"Choose stock invest in\n {stocks}\n->").lower()

            if stock in stocks:
                stock_price = r(1,wealth)
                print(f"Price of this stock is {stock_price}")
                print(f"Your wealth : {wealth}")
                
                amount =  int(input("Enter the amount you would like to invest\n ->"))
                
                if  amount <= wealth :
                    r_letter = random.choice(["a","b"])
                    if r_letter == "a":
                        time.sleep(1)
                        print("Stock price is increasing you will profit!")
                        wealth += int(amount/2)
                        time.sleep(1)
                        print(f"Your wealth incresed :{wealth}")

                    elif r_letter == "b":
                        time.sleep(1)
                        print("Stock price is decresing you will lose!")
                        wealth -= int(amount)
                        time.sleep(1)
                        print(f"Your wealth decreased:{wealth}")
                    else :
                        print("invalid input.")
                else:
                    print("You do not have enough wealth.")
                    continue

            if stock == "exit":
                print("you are moving to luxury life")
                luxury(wealth)
                break

         return wealth
                

def luxury(wealth):
    print(f"Your wealth is : {wealth}")
    wealth = round(wealth/6,2)
    
    if wealth >= 90:
        print(f"You lived {wealth} year's of luxurious life. {time.sleep(1)}\n You died of old age.\n {time.sleep(0.5)}YOU WON!!!")
    else:
        print(f" You died at early age .\n YOU LOSE!!!")


dungean()