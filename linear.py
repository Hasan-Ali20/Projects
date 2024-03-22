# Import necessary libraries used in linear regression, data manipulation and visualisation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Import the insurance data from the CSV file
insurance = pd.read_csv("insurance.csv")

# Selects only the "Age" and "Charges" columns for analysis 
df = insurance [["age", "charges"]]

# Part a: Scatter plot with age on the x-axis and charges on the y-axis

x = ["age"]
y = ["charges"]

# The data will be used for linear regression, and reshapes into a 2-dimensional array
x = df["age"].values.reshape(-1, 1)
y = df["charges"].values

# Part b: Using linear_model.LinearRegression() from sklearn, fit a model to your data, and make predictions ond data

# Use LinearRegression to fit the model
insurance_model = LinearRegression()
insurance_model.fit(x,y)

# Plot the data and model to make predictions
y_pred = insurance_model.predict(x)

# Part c: Scatter plot with the best-fit line
# Scatter plot of the data points
plt.scatter(x,y,color = "b")

# Line plot of the model's prediction
plt.plot(x,y_pred,color = "r")
plt.xlabel("Age")
plt.ylabel("Charges")
plt.show()

# Using a random age to make a prediction
user_age = int(input("Please enter your age, based on this we will calculate your insurance charges: "))
unk_x = [[user_age]]

# Append the new age to the existing age array
x_pred = np.append(x, unk_x).reshape(-1,1)
# Predict the insurance charges for all ages including the random age
y_pred = insurance_model.predict(x_pred)

# Visualise the predictions with the random age included
plt.scatter(x,y,color = "b")
plt.plot(x_pred,y_pred,color = "r")
plt.xlabel("Age")
plt.ylabel("Charges")
plt.show()

# Display the predicted charges for the random age
predicted_charge = insurance_model.predict(unk_x)[0]
print(f"Insurance charges should be £{predicted_charge:.2f} for your age of {user_age}.")
