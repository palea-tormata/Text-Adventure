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
    # print a list of places (string format) you can move to    
    def where_can_I_go(self):
        where = []
        for pos in where_to[self.position]:
            where.append(location_names[pos])
        print(where)
    def move(self):
        self.where_can_I_go()
        to = raw_input("Where to? > ")
        if to not in location_names:
            print("You can't go there..")
        else:
            self.position = location_names.index(to)
        
