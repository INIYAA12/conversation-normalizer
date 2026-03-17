from fastapi import FastAPI
from pydantic import BaseModel
from nlp.normalizer import normalize_text

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Conversation Normalizer running"}

@app.post("/normalize")
def normalize(data: TextInput):

    result = normalize_text(data.text)

    return {
        "original": data.text,
        "normalized": result
    }