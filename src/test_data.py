import pandas as pd

# Load dataset
ratings = pd.read_csv("data/ratings.csv")

# Take subset for performance
ratings = ratings.head(100000)

print("Dataset Loaded Successfully!\n")
print(ratings.head())

print("\nShape of dataset:", ratings.shape)