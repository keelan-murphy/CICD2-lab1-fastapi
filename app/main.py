from fastapi import FastAPI

app = FastAPI(titel="Lab 1 - FastAPI")

@app.get("/health")
def health():
    return{"status": "ok"}

@app.get("/hello") 
def hello(): 
    return {"message": "Some Message"} 