# Handle It
# Demonstrates handling exceptions
# try/except
chk=True
while chk:
 try:
  num = float(input("Enter a number: "))
  chk=False
 except:
  print("Please only Enter a number !")

print(num)