from pydantic import BaseModel

class todo(BaseModel):
    name:str
    field1:str
    completed:bool