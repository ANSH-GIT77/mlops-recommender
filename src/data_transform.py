import pandas as pd

# Load dataset
ratings = pd.read_csv("data/ratings.csv")

# Take subset for performance
ratings = ratings.head(100000)

# Convert ratings to interactions
def convert_interaction(rating):
    if rating >= 4:
        return "purchase"
    elif rating == 3:
        return "click"
    else:
        return "view"

ratings["interaction"] = ratings["rating"].apply(convert_interaction)

# Rename columns to match e-commerce format
ratings.rename(columns={
    "userId": "user_id",
    "movieId": "product_id"
}, inplace=True)

# Save processed data
ratings.to_csv("data/processed_data.csv", index=False)

print("Data Transformation Completed!\n")
print(ratings.head())