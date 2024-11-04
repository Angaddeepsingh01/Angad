
# Multiplayer Game


from random import randint as r 


def mult_ply():

    players = input("How many players (2-4): ")

    # list of players 
    ply_list = [] 

    if players.isdigit() and int(players) in [2,3,4]:

        players = int(players)

        ply_list = [0 for _ in range (players)] 

        print(ply_list)

        current_player = 0

        while True:
            num = r(1,2)

            # print(num)

            print(f"{current_player + 1} player's turn")
            guess = int(input("Please enter your guess (1-2): "))
        
     
            if guess == num :

                print("you guessed right! , you get a point")
                
                ply_list[current_player] += 1 

                print(f"Scores : {ply_list}")
                num = r(1,2)

            else:
                
                print("you guessed wrong, you don't get a point")

                print(f"Scores : {ply_list}")

                current_player = (current_player + 1) % players

mult_ply()



