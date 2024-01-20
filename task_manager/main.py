"""
Main Function Execution for the Task Manager
"""
import os
from sqlmodel import Session
from task_manager.db import DB
from task_manager.logger import create_logger
from task_manager.model import Tasks, TaskStatus


# Extract the filename without extension
filename = os.path.splitext(os.path.basename(__file__))[0]

logger = create_logger(logger_name=filename)

if __name__ == "__main__":
    # Create a Task
    task1 = Tasks(
        title="Go to the Gym",
        description="Visit Gym at 09:00",
        status=TaskStatus.NOT_STARTED,
    )
    task2 = Tasks(
        title="Buy Groceries",
        description="Large shopping list - buy at 12:00",
        status=TaskStatus.NOT_STARTED,
    )

    # Create a DB Instance
    db = DB()

    # Create a Session
    session = Session(db.engine)

    # Write Task to DB
    # db.create_task(task=task1, session=session)
    # db.create_task(task=task2, session=session)

    # Read Task from DB
    # task = db.read_task(task_id=5, session=session)
    # print(task.description)

    # Read All Tasks from DB
    # tasks = db.read_tasks(session=session)
    # print(tasks)
    # for task in tasks:
    #     print(task.title)

    # Update task2
    # db.update_task(
    #     session=session,
    #     task_id=2,
    #     task_status=TaskStatus.COMPLETED,
    # )

    # Delete task2
    # db.delete_task(session=session, task_id=1)

    # Delete all tasks
    # db.delete_all_tasks(session=session)
