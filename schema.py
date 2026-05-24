from pydantic import BaseModel, Field,field_validator
from enum import Enum
from datetime import date 

class PriorityEnum(str,Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TaskBase(BaseModel):
    @field_validator('due_date')
    def validate_due_date(cls, value):
        if value and value < date.today():
            raise ValueError("Due date cannot be in the past")
        return value

class TaskCreate(TaskBase):
    title:str =Field(min_length=3,max_length=100)
    description:str| None =Field(default=None, min_length=3,max_length=100)
    completed:bool=False
    priority:PriorityEnum
    category: str=Field(min_length=3)
    due_date:date | None = None

    @field_validator('due_date')
    def validate_due_date(cls, value):
        if value and value < date.today():
            raise ValueError("Due date cannot be in the past")
        return value
    
class TaskUpdate(TaskBase):
    title:str | None =Field(default=None, min_length=3,max_length=100)
    description:str| None=Field(default=None, min_length=3,max_length=100)
    category: str | None = Field(default=None, min_length=3)
    completed:bool | None =None
    priority:PriorityEnum | None = None
    due_date:date | None = None

    @field_validator('due_date')
    def validate_due_date(cls, value):
        if value and value < date.today():
            raise ValueError("Due date cannot be in the past")
        return value