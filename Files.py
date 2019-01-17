file=open("text.txt","w")
file.write("Demo")
file.close()

file=open("text.txt","r")
print(file.read())