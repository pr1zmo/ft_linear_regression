import pandas as pd
import numpy as np
import sys
# import matplotlib.pyplot as plt

def train(path: str) -> any:
	"""
	The train function is used to train the model

	It will read data from data.csv and perform a linear regression on the data.

	Once the linear regression has completed, it will save the variables theta0 and
	theta1 for use in the first program (predict)

	tmpθ0 = learningRate ∗1/m m−1∑i=0 (estimatePrice(mileage[i]) − price[i])
	"""	
	qoeficient = 0
	x = -1
	try:
		data = pd.read_csv(path)
		df = pd.DataFrame(data)
		# df.plot()
		# plt.plot(df)
		theta0 = df['km']
		theta1 = df['price']
		if (len(theta0) != len(theta1)):
			raise ValueError("Mismatch in data lengths: 'km' and 'price' columns must have the same length")
		for i in range(len(theta0) - 1):
			if (i != 0):
				x = 0
			if (x == -1):
				continue
			qoeficient = (theta0[i - 1] * theta1[i]) / theta1[i - 1]
			qoeficient = (qoeficient + theta0[i]) / 2
		print(qoeficient)	

	except Exception as e:
		print(f"Error: {e}")
		return None
	finally:
		return (theta0, theta1)

# print(train)
train(sys.argv[1])

