list = []
while(True):
    print("""


0. Exit
1. Add
2. Del
3. Show
4. Sort

""")

    choice=input("Enter your choice-")
    if choice=="0":
        print("Bye")
    elif choice=="1":
        list.append(input("Enter to add"))
    elif choice=="2":
        score =input("Which score")
        if score in list:
            list.remove(score)
        else:
            print("Score nor present")
    elif choice=="3":
        for i in list:
            print("The score are-",i)
    elif choice=="4":
        list.sort()
