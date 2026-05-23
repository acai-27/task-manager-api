from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud
from app.schema import TaskCreate, TaskUpdate
from app.db import SessionLocal
router=APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_tasks(db:Session=Depends(get_db)):
    return crud.get_tasks(db)

@router.get("/{task_id}")
def read_task(task_id: int ,db:Session=Depends(get_db)):
    return crud.get_task(task_id, db)

@router.post("/")
def create_tasks(task: TaskCreate,db:Session=Depends(get_db)):
    return crud.create_tasks(task, db)

@router.put("/{task_id}")
def update_task(task_id:int,task: TaskUpdate,db:Session=Depends(get_db)):
    return crud.update_task(task_id, task, db)

@router.delete("/{task_id}")
def delete_task(task_id:int,db:Session=Depends(get_db)):
    return crud.delete_task(task_id, db)   

