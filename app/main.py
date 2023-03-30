from fastapi import FastAPI
from .routes.route import api_router

app = FastAPI()

app.include_router(api_router)
@app.get("/")
async def index():
    return {"message":"index page"}