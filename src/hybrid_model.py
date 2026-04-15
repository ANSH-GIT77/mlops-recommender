import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load datasets
data = pd.read_csv("data/processed_data.csv")

# 🔥 IMPORTANT FIX: Limit movies to avoid memory crash
movies = pd.read_csv("data/movies.csv").head(5000)

# -------------------------------
# COLLABORATIVE FILTERING PART
# -------------------------------

interaction_map = {
    "view": 1,
    "click": 2,
    "purchase": 3
}

data["interaction_score"] = data["interaction"].map(interaction_map)

user_item_matrix = data.pivot_table(
    index="user_id",
    columns="product_id",
    values="interaction_score",
    fill_value=0
)

user_similarity = cosine_similarity(user_item_matrix)

user_similarity_df = pd.DataFrame(
    user_similarity,
    index=user_item_matrix.index,
    columns=user_item_matrix.index
)

# -------------------------------
# CONTENT-BASED FILTERING PART
# -------------------------------

tfidf = TfidfVectorizer(stop_words='english')

movies["title"] = movies["title"].fillna("")

tfidf_matrix = tfidf.fit_transform(movies["title"])

# 🔥 FIX: Compute similarity only when needed (not full matrix)
def get_similar_items(movie_id, top_n=5):
    if movie_id not in movies["movieId"].values:
        return []

    idx = movies[movies["movieId"] == movie_id].index[0]
    similarity_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()

    similar_indices = similarity_scores.argsort()[::-1][1:top_n+1]
    return movies.iloc[similar_indices]["movieId"].values

# -------------------------------
# HYBRID RECOMMENDATION FUNCTION
# -------------------------------

def hybrid_recommend(user_id, top_n=5):
    
    # Collaborative recommendations
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)[1:6]

    collab_products = set()
    for sim_user in similar_users.index:
        products = user_item_matrix.loc[sim_user]
        top_products = products[products > 0].sort_values(ascending=False).head(5)
        collab_products.update(top_products.index)

    # Content-based recommendations
    user_products = data[data["user_id"] == user_id]["product_id"].values
    
    content_products = set()
    if len(user_products) > 0:
        last_product = user_products[-1]
        similar_items = get_similar_items(last_product)
        content_products.update(similar_items)

    # Combine both
    final_recommendations = list(collab_products.union(content_products))

    return final_recommendations[:top_n]


# -------------------------------
# TEST
# -------------------------------

print("\nHybrid Recommendations for User 1:")
print(hybrid_recommend(1))