inventory = ["sword", "armor", "shield", "healing potion"]
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("Enter the index number to end the slice: "))
print("inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])
inventory[1:6] = ["orb of future telling"]
print("Your inventory is now:")
print(inventory)
input("\nPress the enter key to continue.")