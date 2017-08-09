import json
import os

def get_object(name, loc):
    ret = None
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    with open(fileDir + "/obj/" + str(name) + ".json", "r") as f:
        jsontext = f.read()
        d = json.loads(jsontext)
        d['location'] = loc 
        ret = Object(**d)
    return ret

class Object():
    def __init__(self, name="Location", description="", location = 0, interact = {}):
        self.name = name
        self.description = description
        self.location = location
        self.interact = interact
    def _info(self):
        print(self.name + " -- " + self.description)
    def _name(self):
        return self.name
    def poke(self):
        return self.interact['poke']
    def take(self):
        return self.interact['take']
