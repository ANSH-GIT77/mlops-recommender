import sys
import os
from api.monitor import router as monitor_router

# ✅ FORCE add project root to Python path (FINAL FIX)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.hybrid_model import hybrid_recommend
from src.logger import get_logger

# Initialize FastAPI app
app = FastAPI()
app.include_router(monitor_router)

# Logger setup
logger = get_logger()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# ROOT ENDPOINT
# -----------------------------
@app.get("/")
def home():
    return {"message": "AI Recommendation System API is Running 🚀"}

# -----------------------------
# RECOMMENDATION ENDPOINT
# -----------------------------
@app.get("/recommend")
def recommend(user_id: int):
    try:
        logger.info(f"Request for user_id: {user_id}")

        recommendations = hybrid_recommend(user_id)

        logger.info(f"Recommendations: {recommendations}")

        return {
            "user_id": user_id,
            "recommendations": recommendations
        }

    except Exception as e:
        logger.error(f"Error: {str(e)}")

        return {
            "error": "Something went wrong",
            "details": str(e)
        }