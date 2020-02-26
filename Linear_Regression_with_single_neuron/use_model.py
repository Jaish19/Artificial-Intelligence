from sklearn.externals import joblib

# Load our trained model
model = joblib.load('house_value_model.pkl')

# Define the house that we want to value (with the values in the same order as in the training data)
house_1 = [
    2000,  # Size in Square Feet
    3,  # Number of Bedrooms
    2,  # Number of Bathrooms
]

# scikit-learn assumes you want to predict the values for multiple of houses at once, so it expects an array.
# We only want to estimate the value of a single house, so there will only be one item in our array.
homes = [
    house_1
]

# Make a prediction for each house in the homes array (we only have one)
home_values = model.predict(homes)

# Since we are only predicting the price of one house, grab the first prediction returned
predicted_value = home_values[0]

# Print the results
print("House details:")
print(f"- {house_1[0]} sq feet")
print(f"- {house_1[1]} bedrooms")
print(f"- {house_1[2]} bathrooms")
print(f"Estimated value: ${predicted_value:,.2f}")

