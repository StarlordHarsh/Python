# Attribute Critter
# Demonstrates creating and accessing object attributes
class Critter(object):
 """A virtual pet"""
 def __init__(self, name):
    print("A new critter has been born!")
    self.name = name
 def __str__(self):
    rep = "Critter object\n"
    rep += "name: " + self.name + "\n"
    return rep
 def talk(self):
    print("Hi. I'm", self.name, "\n")
# main
crit1=Critter(input("Enter the name of critter 1"))
crit1.talk()
crit2 = Critter(input("Enter the name of critter 2"))
crit2.talk()
print("Printing crit1:")
print(Critter)
print("Directly accessing crit1.name:")
print(Critter.name)
print("Printing crit1:")
print(crit2)
print("Directly accessing crit1.name:")
print(crit2.name)
