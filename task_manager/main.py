from sqlmodel import SQLModel, Session
from model import Tasks, TaskStatus
from db import DB

if __name__ == "__main__":
    # Create a Task
    task = Tasks(
        title="Test Task",
        description="This is a test task",
        status=TaskStatus.IN_PROGRESS,
    )

    # Create a DB Instance
    db = DB()

    # Write Task to DB
    task_id = db.create_task(task)
    print(task_id)
