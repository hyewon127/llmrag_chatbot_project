from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():

    # 서버 동작 확인용

    return {
        "message":"rag server running"
    }
