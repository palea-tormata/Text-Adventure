location_names = ["Castle","East Bridge","West Bridge","Woods","Lake"]
where_to = [[1,2],[0,3],[0,4],[1],[2]]

class Player:
    def __init__(self, name, position, hp):
        self.name = name
        self.position = position
        self.hp = hp
    def my_name(self):
        print("Your name is " + self.name)
    def my_health(self):
        print("You have " + self.hp + " hp")    
    def where_am_I(self):
        print("You are at the " + location_names[self.position])

    def move(self):
        print(where_can_I_go(self))
        to = raw_input("Where to? > ")
        if to not in location_names:
            print("You can't go there..")
        else:
            self.position = location_names.index(to)
        

# return a list of places (string format) you can move to
def where_can_I_go(player):
    where = []
    for pos in where_to[player.position]:
        where.append(location_names[pos])
    return where
        




if __name__ == "__main__":
    # player is prompted to input a name
    player_name = raw_input("Enter your name > ")
    # select difficulty -> different starting hp
    difficulty  = raw_input("Select difficulty (Easy, Medium, Hard) > ")
    # TODO input clean-up required
    
    if difficulty == "Easy":
        starting_hp = 20
    elif difficulty == "Medium":
        starting_hp = 15
    else:
        starting_hp = 10

    # starting position is at the Castle
    player = Player(player_name, 0, starting_hp)

    print("The game has started!")
    while True:
        action = raw_input(" > ")
    
        if action == "quit":
            break
        elif action == "move":
            player.move()
        elif action == "where":
            print(where_can_I_go(player))

    print("Thank you for playing")
    exit(0) 
