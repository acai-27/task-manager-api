from pydantic import BaseModel

class TaskCreate(BaseModel):
    title:str
    description:str
    completed:bool=False
    priority:str
    
class TaskUpdate(BaseModel):
    title:str | None=None
    description:str | None=None
    completed:bool | None=None
    priority:str | None=None