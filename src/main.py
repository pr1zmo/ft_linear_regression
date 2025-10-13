from predict import predict
from train import train

def main():
	predict("predict")
	print(predict.__doc__)
	train("train")
	print(train.__doc__)

if __name__ == "__main__":
	main()