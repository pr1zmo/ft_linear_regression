def train(object: any) -> any:
	"""
	The train function is used to train the model

	It will read data from data.csv and perform a linear regression on the data.

	Once the linear regression has completed, it will save the variables theta0 and
	theta1 for use in the first program (predict)

	tmpθ0 = learningRate ∗1/m m−1∑i=0 (estimatePrice(mileage[i]) −price[i])
	"""
	print("Hello " + str(object))