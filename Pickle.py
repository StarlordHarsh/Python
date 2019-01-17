import pickle, shelve
print("Pickling")
f=open("Pickles.dat","wb")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
pickle.dump(variety,f)
pickle.dump(shape,f)
f.close()

print("Unpickling")
f=open("Pickles.dat", "rb")
print(pickle.load(f))
print(pickle.load(f))
f.close()