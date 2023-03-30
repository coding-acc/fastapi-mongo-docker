from fastapi import APIRouter
from ..config.database import collection
from ..models.model import todo
from ..schemas.schema import serializer, serializers
from bson import ObjectId

api_router = APIRouter()

#retrieve

@api_router.get("/")
async def get_todos():
    todos = serializers(collection.find())
    return {"status":"ok", "data":todos}

@api_router.get("/{id}")
async def get_todo(id:str):
    todo = serializers(collection.find({"_id":ObjectId(id)}))
    return {"status":"ok", "data":todo}

@api_router.post("/")
async def post_todo(todo:todo):
    _id = collection.insert_one(dict(todo))
    todo = serializers(collection.find({"_id":_id.inserted_id}))
    return {"status":"ok", "data":todo}