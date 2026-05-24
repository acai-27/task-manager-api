from app.schema import SortOrderEnum, TaskCreate
from app.schema import TaskUpdate
from app.model import Task
from sqlalchemy.orm import Session 

def create_tasks(task: TaskCreate, db: Session):
    db_task=Task(
        title=task.title,
        description=task.description,
        completed=task.completed,
        priority=task.priority,
        category=task.category,
        due_date=task.due_date
        )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(priority,category,completed,sort_order,limit,offset,db: Session):
    query = db.query(Task)
    if priority is not None:
        query = query.filter(Task.priority == priority)
    if category is not None:
        query = query.filter(Task.category == category)
    if completed is not None:
        query = query.filter(Task.completed == completed)
    if sort_order == SortOrderEnum.ASC:
        query=query.order_by(Task.due_date.asc())
    elif sort_order == SortOrderEnum.DESC:
        query=query.order_by(Task.due_date.desc())
    return query.offset(offset).limit(limit).all()

def get_task(task_id: int, db: Session):
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(task_id: int, task: TaskUpdate, db: Session):
    db_existing_task=get_task(task_id,db)
    if not db_existing_task:
        return None
    update_data=task.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_existing_task, key, value)
    db.commit()
    db.refresh(db_existing_task)
    return db_existing_task

def delete_task(task_id:int,db:Session):
    db_task=get_task(task_id,db)
    if not db_task:
        return None
    db.delete(db_task)
    db.commit()
    return db_task