import json
import numpy as np
import matplotlib.pyplot as plt
f = open("./data.json","r")
#data = f.read()
#print(data)
data = json.load(f)

poids = np.array([])
for person in data:
    poids = np.append(poids,person["Weight"])

moyennePoids = np.mean(poids)
print(f"poids moyen est {moyennePoids}")

heights = np.array([])
for person in data:
    heights = np.append(heights,person["Height"])
heights = heights/100

moyenneHeights = np.mean(heights)
print(f"height moyen est {moyenneHeights}")

bmis = poids/heights**2

names  = np.array([])
for person in data:
    names = np.append(names,person["Name"])

indices = np.where(bmis>25)
print("la liste des personnes qui sont obeses:")
for i in np.array(indices).reshape(-1):
    print(f"- {names[i]}, bmi = {bmis[i]}, height = {heights[i]}m , weight = {poids[i]}kg")

median=np.median(poids)
print(median)

plt.hist(bmis, bins=20, color='blue', edgecolor='black',histtype="bar")
plt.title('BMI Distribution')
plt.xlabel('BMI')
plt.ylabel('Frequency')
plt.show()

# mehdi.tmimi@usmba.ac.ma