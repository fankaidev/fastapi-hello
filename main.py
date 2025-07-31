from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/hello")
def get_hello():
    current_date = datetime.now().isoformat()
    return {"message": f"hello {current_date}"}

@app.get("/health")
def health_check():
    return {"status": "OK"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)