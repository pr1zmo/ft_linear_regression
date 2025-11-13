import matplotlib.pyplot as plt
import numpy as np

def display_data(theta0: any, theta1: any):
	plt.scatter(theta0, theta1, s=15, color="#ffc300", alpha=0.8, label="Data")

	# Compute and draw a simple linear fit line (average)
	a, b = np.polyfit(theta0, theta1, 1)   # slope and intercept
	x_line = np.linspace(min(theta0), max(theta0), 100)
	y_line = a * x_line + b
	plt.plot(x_line, y_line, color="blue", linewidth=2, label="Linear Fit")

	plt.xlabel("Kilometers")
	plt.ylabel("Price")
	plt.legend()
	plt.grid(True)
	plt.title("Price in relation to Kilometers")
	plt.xlim(left=0)
	plt.ylim(bottom=0)
	plt.show()