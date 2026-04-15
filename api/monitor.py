from fastapi import APIRouter
import os

router = APIRouter()

LOG_FILE = "logs/app.log"

@router.get("/logs")
def get_logs():
    if not os.path.exists(LOG_FILE):
        return {"message": "No logs found"}

    with open(LOG_FILE, "r") as file:
        logs = file.readlines()

    return {"logs": logs[-20:]}


@router.get("/stats")
def get_stats():
    if not os.path.exists(LOG_FILE):
        return {"total_requests": 0}

    with open(LOG_FILE, "r") as file:
        logs = file.readlines()

    # ✅ COUNT ANY REQUEST LOG
    total_requests = sum(1 for log in logs if "user_id" in log)

    return {
        "total_requests": total_requests
    }