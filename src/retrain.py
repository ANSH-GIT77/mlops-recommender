import sys
import os
import time

# ✅ Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.hybrid_model import hybrid_recommend
from src.logger import get_logger

# Initialize logger
logger = get_logger()


def check_new_data():
    """
    Check if new data is added by monitoring file modification time
    """
    data_path = "data/processed_data.csv"

    # Get last modified time
    last_modified = os.path.getmtime(data_path)

    # First time setup
    if not hasattr(check_new_data, "last_checked"):
        check_new_data.last_checked = last_modified
        return False

    # If file changed → new data
    if last_modified != check_new_data.last_checked:
        check_new_data.last_checked = last_modified
        return True

    return False


def retrain_model():
    """
    Simulate retraining process + versioning
    """
    print("🔄 New data detected! Retraining model...")
    logger.info("Retraining started")

    # Run model once (simulation)
    recs = hybrid_recommend(user_id=1)

    # ✅ Model versioning using timestamp
    version = int(time.time())
    model_path = f"models/model_{version}.onnx"

    # Dummy save (simulate model saving)
    with open(model_path, "w") as f:
        f.write("dummy model data")

    print(f"✅ Model retrained & saved as {model_path}")
    print("Sample Output:", recs)

    logger.info(f"Model retrained and saved: {model_path}")
    logger.info(f"Sample recommendations: {recs}")


def main():
    print("🚀 Retraining service started...")
    logger.info("Retraining service started")

    while True:
        try:
            if check_new_data():
                retrain_model()
            else:
                print("⏳ No new data... waiting...")
            
            time.sleep(10)

        except Exception as e:
            print("❌ Error in retraining:", str(e))
            logger.error(f"Error in retraining: {str(e)}")
            time.sleep(5)


if __name__ == "__main__":
    main()