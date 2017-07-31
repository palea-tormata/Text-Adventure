from player import Player

# TODO 
# input clean-up required (case sensitive)
# unexpected input
# list the possibilities for given situation

if __name__ == "__main__":
    # player is prompted to input a name
    player_name = raw_input("Enter your name > ")
    # select difficulty -> different starting hp
    difficulty  = raw_input("Select difficulty (Easy, Medium, Hard) > ")
    
    if difficulty == "Easy":
        starting_hp = 20
    elif difficulty == "Medium":
        starting_hp = 15
    elif difficulty == "Hard":
        starting_hp = 10
    else:
        print("That's not an option")
        exit(1)

    # starting position is at the Castle (0)
    player = Player(player_name, 0, starting_hp)

    print("The game has started!")
    while True:
        action = raw_input(" > ")
    
        if action == "quit":
            break
        elif action == "move":
            player.move()
        elif action == "where":
            player.where_can_I_go()
        else:
            print("That's not an option")
            exit(1)

    print("Thank you for playing")
    exit(0) 
