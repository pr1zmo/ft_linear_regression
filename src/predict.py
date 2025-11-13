import pandas as pd
import numpy as np
from train import train

def predict(file_n: str, mileage: float) -> any:
	"""
   The first program will be used to predict the price of a car for a given mileage.

   When you launch the program, it should prompt you for a mileage, and then give
   you back the estimated price for that mileage. The program will use the following
   hypothesis to predict the price:

	estimatePrice(mileage) = thedata0 + (thedata1 ∗ mileage)
	"""
	theta0, theta1 = 0, 0
	price = theta0 + (theta1 * mileage)
	print("Price before the training: " + str(price))
	theta0, theta1 = train(file_n)
	price = theta0 + (theta1 * mileage)
	print("After the training: " + str(price))