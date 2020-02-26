from keras.models import load_model
from sklearn.externals import joblib

# Load our trained model
model = load_model('house_value_model.h5')

# Load the data scalers so that we can transform new data and prediction the same way as training data.
X_scaler = joblib.load('X_scaler.pkl')
y_scaler = joblib.load('y_scaler.pkl')

# Define the house that we want to value (with the values in the same order as in the training data).
house_1 = [
    2000,  # Size in Square Feet
    3,  # Number of Bedrooms
    2,  # Number of Bathrooms
]

# Keras assumes we want to predict the values for multiple of houses at once, so it expects an array.
# We only want to value a single house, so it will be the only item in our array.
homes = [
    house_1
]

# Scale the new data like the training data
scaled_home_data = X_scaler.transform(homes)

# Make a prediction for each house in the homes array (but we only have one)
home_values = model.predict(scaled_home_data)

# The prediction from the neural network will be scaled 0 to 1 just like the training data
# We need to unscale it using the same factor as we used to scale the training data
unscaled_home_values = y_scaler.inverse_transform(home_values)

# Since we are only predicting the price of one house, grab the first prediction returned
predicted_value = unscaled_home_values[0][0]

# Print the results
print("House details:")
print(f"- {house_1[0]} sq feet")
print(f"- {house_1[1]} bedrooms")
print(f"- {house_1[2]} bathrooms")
print(f"Estimated value: ${predicted_value:,.2f}")

