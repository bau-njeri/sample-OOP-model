class vehicle:
    wheels=0
    color=''
    def hoot(self):
        print("peeep")

    def color (self):
        print(self.color)
class truck(vehicle):
    def gas(self):
        print("i use diesel")
class bus(vehicle):
    def seat(self):
        print("i have over 10 seats")
        
 
