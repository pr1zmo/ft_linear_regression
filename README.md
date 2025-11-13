# ft_linear_regression

A basic machine learning implementation that predicts car prices based on mileage using linear regression with gradient descent optimization.

## 📖 Overview

This project implements a simple linear regression algorithm from scratch to predict the price of a car given its mileage. The model uses the gradient descent algorithm to train on historical data and learn the relationship between kilometers driven and car price.

The prediction follows the linear hypothesis:
```
estimatePrice(mileage) = θ₀ + (θ₁ × mileage)
```

Where:
- `θ₀` (theta0) is the intercept
- `θ₁` (theta1) is the slope coefficient

## 🚀 Features

- **Training Module**: Implements gradient descent algorithm to learn optimal parameters
- **Prediction Module**: Estimates car prices based on trained model
- **Data Normalization**: Uses feature scaling for improved gradient descent stability
- **Visualization**: Displays data points and fitted linear regression line
- **CSV Data Support**: Reads training data from CSV files

## 📁 Project Structure

```
ft_linear_regression/
├── src/
│   ├── main.py        # Main entry point
│   ├── train.py       # Training logic with gradient descent
│   ├── predict.py     # Prediction functionality
│   └── display.py     # Data visualization
├── data/
│   ├── data.csv                    # Training dataset
│   └── car_price_synthetic.csv     # Additional synthetic dataset
├── docs/
│   └── linear_regression.pdf       # Project documentation
├── Makefile           # Build and run commands
└── README.md
```

## 🛠️ Installation

### Requirements

- Python 3.x
- pandas
- numpy
- matplotlib

### Setup

```bash
# Clone the repository
git clone https://github.com/pr1zmo/ft_linear_regression.git
cd ft_linear_regression

# Install dependencies
pip install pandas numpy matplotlib
```

## 💻 Usage

### Running the Program

Using Make:
```bash
make run
```

Or directly with Python:
```bash
python3 src/main.py
```

### Input Format

The program will prompt you for:
1. **Training data file path**: Path to your CSV file (e.g., `data/data.csv`)
2. **Mileage**: The mileage for which you want to predict the price

### Example

```
Please Enter the training data file: data/data.csv
Please enter the mileage of the car: 50000
Price before the training: 0
Training completed:
θ₀ = 8500.1234, θ₁ = -0.021345
After the training: 7432.85
```

## 📊 Data Format

The CSV file should contain two columns:
- `km`: Mileage in kilometers
- `price`: Car price

Example:
```csv
km,price
240000,3650
139800,4900
150500,5100
```

## 🧮 Algorithm Details

### Gradient Descent Implementation

1. **Initialization**: Parameters θ₀ and θ₁ start at 0
2. **Normalization**: Input features are normalized using mean and standard deviation
3. **Iteration**: Runs for 10,000 iterations with a learning rate of 0.01
4. **Gradient Calculation**: 
   - `grad₀ = (1/m) × Σ(errors)`
   - `grad₁ = (1/m) × Σ(errors × x_norm)`
5. **Parameter Update**:
   - `θ₀ = θ₀ - α × grad₀`
   - `θ₁ = θ₁ - α × grad₁`
6. **Denormalization**: Parameters are converted back to original scale

### Hyperparameters

- **Learning rate (α)**: 0.01
- **Iterations**: 10,000
- **Initial θ₀, θ₁**: 0.0

## 📈 Visualization

The `display.py` module provides visualization of:
- Training data points (scatter plot)
- Fitted linear regression line
- Grid and labels for better readability

## 🧹 Cleaning

To remove Python cache files:
```bash
make clean
```

## 📚 Documentation

Additional documentation about linear regression theory can be found in `docs/linear_regression.pdf`.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements.

## 📝 License

This project is part of the 42 School curriculum.

## 👤 Author

**pr1zmo**
- GitHub: [@pr1zmo](https://github.com/pr1zmo)

---

*This project demonstrates fundamental machine learning concepts including supervised learning, linear regression, and gradient descent optimization.*
