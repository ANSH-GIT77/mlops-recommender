import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load processed data
data = pd.read_csv("data/processed_data.csv")

# Convert interaction to numeric weight
interaction_map = {
    "view": 1,
    "click": 2,
    "purchase": 3
}

data["interaction_score"] = data["interaction"].map(interaction_map)

# Create user-item matrix
user_item_matrix = data.pivot_table(
    index="user_id",
    columns="product_id",
    values="interaction_score",
    fill_value=0
)

print("User-Item Matrix Created!")

# Compute similarity between users
user_similarity = cosine_similarity(user_item_matrix)

print("User Similarity Matrix Created!")

# Convert to DataFrame
user_similarity_df = pd.DataFrame(
    user_similarity,
    index=user_item_matrix.index,
    columns=user_item_matrix.index
)

# Recommendation function
def recommend_products(user_id, top_n=5):
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)[1:6]

    recommended_products = set()

    for sim_user in similar_users.index:
        products = user_item_matrix.loc[sim_user]
        top_products = products[products > 0].sort_values(ascending=False).head(5)
        recommended_products.update(top_products.index)

    return list(recommended_products)[:top_n]


# Test recommendation
print("\nSample Recommendations for User 1:")
print(recommend_products(1))