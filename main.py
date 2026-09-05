from fastapi import FastAPI

from src.routes.characterRoute import router as character_router

app = FastAPI()
app.include_router(character_router)

@app.get("/")
def root():
	return {"message": "Hello D&D"}
