def create_tasks(task: schema.TaskCreate, db: Session):
    db_task=model.Task(
        title=task.title,
        description=task.description,
        completed=task.completed,
        priority=task.priority
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session):
    return db.query(model.Task).all()

def get_task(task_id: int, db: Session):
    return db.query(model.Task).filter(model.Task.id == task_id)