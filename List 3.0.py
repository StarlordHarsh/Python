scores = []
choice = None
while choice != "0":
 print(
 """
 High Scores 2.0
 0 - Quit
 1 - List Scores
 2 - Add a Score
 """
 )
 choice = input("Choice: ")
 print()
 if choice == "0":
  print("Good-bye.")
 elif choice=="1":
     print("Name\tScores")
     for entry in scores:
         score, name=entry
         print(score,"\t",name)
 elif choice=="2":
     name = input("enter the name")
     score = int(input("Enter score"))
     entry=name,score
     scores.append(entry)

