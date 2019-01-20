class Critter(object):
 """A virtual pet"""
 total = 0
 @staticmethod
 def status():
    print("\nThe total number of critters is", Critter.total)
 def __init__(self, name):
    print("A critter has been born!")
    self.name = name
    Critter.total += 1
#main
choice=1
print("Accessing the class attribute Critter.total:", end=" ")
print(Critter.total)
print("\nCreating critters.")

while (choice!=0):
    choice=int(input("Press 1 to add critter and 0 to exit"))
    if (choice==1):
        crit=Critter(input("Enter a name of the critter"))

Critter.status()
print("\nAccessing the class attribute through an object:", end= " ")
print(crit.total)