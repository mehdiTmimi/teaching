import numpy as np
import json
import matplotlib.pyplot as plt
f = open("./data.json", "r")
jsonData = f.read()
healthData= json.loads(jsonData)

names = np.array([entry["Name"] for entry in healthData])
heights = np.array([entry["Height"] for entry in healthData])
weights = np.array([entry["Weight"] for entry in healthData])


heights_meters = heights / 100
bmi = weights / (heights_meters ** 2)

# Basic statistics using Numpy
mean_height = np.mean(heights)
mean_weight = np.mean(weights)
mean_bmi = np.mean(bmi)

# Print the results
print(f"Mean Height: {mean_height:.2f} cm")
print(f"Mean Weight: {mean_weight:.2f} kg")
print(f"Mean BMI: {mean_bmi:.2f}")

# Identify individuals with BMI above a certain threshold
threshold_bmi = 25
overweight_individuals = np.where(bmi > threshold_bmi)[0]

print("\nOverweight Individuals:")
for index in overweight_individuals:
    print(f"{names[index]} - Height: {heights[index]:.2f} cm, Weight: {weights[index]:.2f} kg, BMI: {bmi[index]:.2f}")


plt.hist(bmi, bins=20, color='blue', edgecolor='black',histtype="step")
plt.title('BMI Distribution')
plt.xlabel('BMI')
plt.ylabel('Frequency')
plt.show()

underweight = np.sum(bmi < 18.5)
normal_weight = np.sum((bmi >= 18.5) & (bmi < 25))
overweight = np.sum(bmi >= 25)

# Labels and data for the pie chart
labels = ['Underweight', 'Normal Weight', 'Overweight']
sizes = [underweight, normal_weight, overweight]
colors = ['lightcoral', 'lightgreen', 'lightskyblue']

# Plotting the pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Distribution of BMI Categories')

# Show the plot
plt.show()