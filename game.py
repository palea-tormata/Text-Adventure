import cmd
from location import get_location
from obj import get_object

class Game(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        # start at Castle (0)
        self.location = get_location(0)
        self.look()

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
            print(obj.take())
        else:
            print("There is nothing to take here by that name..")
    	

if __name__ == "__main__":
    g = Game()
    g.prompt = '> '
    g.cmdloop()

