import json
import os
from obj import get_object

def get_location(i):
    ret = None
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    with open(fileDir + "/loc/" + str(i) + ".json", "r") as f:
        jsontext = f.read()
        d = json.loads(jsontext)
        #replace name with an object class
        d['objects'] = [get_object(o) for o in d['objects']]            
        ret = Location(**d)
    return ret

class Location():
    def __init__(self, i=0, name="Location", description="", neighbors={}, objects = []):
        self.i = i
        self.name = name
        self.description = description
        self.neighbors = neighbors
        self.objects = objects

    def _neighbor(self, direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None

    def _objects(self):
        if not self.objects:
            print("There's nothing to see here.. move along..")
        else:
            for o in self.objects:
                o._info()

    def obj_in(self, obj_name):
        return next((o for o in self.objects if str(obj_name) == o._name()), None)
    
    def rm_obj(self, obj):
        self.objects.remove(obj)

            
        




        
