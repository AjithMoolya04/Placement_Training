class bird:
    def intro(self):
        print("there are many type of birds")
        
    def flight(self):
        print("most of the birds can fly but some cannot")
        
class sparrow(bird):
    def flight(self):
        print("Sparrows can fly")
        
class ostrich(bird):
    def flight(self):
        print("ostrich cannot fly ")
        
        
obj_bird=bird()
obj_spr=sparrow()
obj_ost=ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

