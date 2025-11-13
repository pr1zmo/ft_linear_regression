import pandas as pd
import numpy as np
import sys
import warnings
warnings.filterwarnings("ignore", message="Unable to import Axes3D")

def train(path: str) -> any:
	"""
	Train the linear regression model using gradient descent.

	Reads the CSV file (columns: km, price),
	fits a linear model y = θ0 + θ1 * x,
	and returns the trained parameters θ0 (intercept) and θ1 (slope).
	"""

	try:
		# Load and validate data
		data = pd.read_csv(path)
		if 'km' not in data.columns or 'price' not in data.columns:
			raise ValueError("CSV must contain 'km' and 'price' columns")

		x = data['km'].values
		y = data['price'].values

		if len(x) != len(y):
			raise ValueError("Mismatch in data lengths: 'km' and 'price' columns must have the same length")

		# Normalize x to improve gradient descent stability
		x_mean = np.mean(x)
		x_std = np.std(x)
		x_norm = (x - x_mean) / x_std

		# Parameters initialization
		theta0 = 0.0  # intercept
		theta1 = 0.0  # slope

		# Training settings
		alpha = 0.01        # learning rate
		iterations = 10000  # number of steps
		m = len(x)

		# Gradient descent loop
		for i in range(iterations):
			# Compute predictions
			predictions = theta0 + theta1 * x_norm

			# Compute errors
			errors = predictions - y

			# Compute gradients
			grad0 = (1 / m) * np.sum(errors)
			grad1 = (1 / m) * np.sum(errors * x_norm)

			# Update parameters
			theta0 -= alpha * grad0
			theta1 -= alpha * grad1

		# Convert θ1 back to original scale
		theta1 = theta1 / x_std
		theta0 = theta0 - theta1 * x_mean

		# Save the trained parameters
		np.savetxt("thetas.csv", [theta0, theta1], delimiter=",")

		print(f"Training completed:\nθ₀ = {theta0:.4f}, θ₁ = {theta1:.6f}")
		return (theta0, theta1)

	except Exception as e:
		print(f"Error: {e}")
		return None
