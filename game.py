import cmd
from location import get_location

class Game(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        # start at Castle (0)
        self.location = get_location(0)
        self.look()
        self.inventory = []

    def do_move(self, direction):
        newlocation = self.location._neighbor(direction)
        if newlocation is None:
            print("You can't go there")
        else:
            self.location = get_location(newlocation)
            self.look()

    def look(self):
        print(self.location.name)
        print("")
        print(self.location.description)
    
    def do_quit(self, args):
        print("Exiting game")
        return True

    def do_see(self, args):
        self.location._objects()

    def do_poke(self, obj):
        obj = self.location.obj_in(obj)
        if obj != None:
            print(obj.poke())
        else:
            print("There is nothing to poke here by that name..")

    def do_take(self, obj):
        obj = self.location.obj_in(obj)
        if obj != None:
            self.location.rm_obj(obj)
            self.inventory.append(obj)
            print(obj.take())
        else:
            print("There is nothing to take here by that name..")

    def do_i(self, args):
        if not self.inventory:
            print("You're not carrying anything at the moment")
        else:
            print("Inventory")
            print("")
            for o in self.inventory:
                o._info()

if __name__ == "__main__":
    g = Game()
    g.prompt = '> '
    g.cmdloop()

