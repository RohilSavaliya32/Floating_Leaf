from fastapi import FastAPI

app = FastAPI(
    title="Floating Translate API",
    description="Translation History Management API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Floating Translate API is running"
    }


# 1. Save Translation
@app.post("/history")
def save_translation():
    return {
        "success": True,
        "message": "Translation saved successfully"
    }


# 2. Get Translation History
@app.get("/history")
def get_history():
    return {
        "success": True,
        "history": []
    }


# 3. Delete Single Translation
@app.delete("/history/{translation_id}")
def delete_translation(translation_id: str):
    return {
        "success": True,
        "message": "Translation deleted",
        "id": translation_id
    }


# 4. Delete All History
@app.delete("/history")
def clear_history():
    return {
        "success": True,
        "message": "All history deleted"
    }
