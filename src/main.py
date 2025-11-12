import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from predict import predict
from train import train

def main():
	predict("predict")
	print(predict.__doc__)
	train("train")
	print(train.__doc__)

if __name__ == "__main__":
	main()