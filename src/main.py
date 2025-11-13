from predict import predict

def main():
	file_m = input("Please Enter the training data file: ")
	mileage = input("Please enter the mileage of the car: ")
	print(predict.__doc__)
	predict(file_m, float(mileage))

if __name__ == "__main__":
	main()