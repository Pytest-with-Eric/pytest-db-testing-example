"""
Database for the Task Manager
"""

from sqlmodel import SQLModel, create_engine, Session
from model import Tasks, TaskStatus


class DB:
    def __init__(self):
        # Create DB Engine
        self.engine = create_engine("sqlite:///database.db", echo=True)
        SQLModel.metadata.create_all(self.engine)

    def create_task(self, task: Tasks) -> int:
        """
        Create a task in the database

        Args:
            task (Tasks): The task to create

        Returns:
            int: The ID of the created task
        """
        # Create a DB Session
        session = Session(self.engine)

        # Write to database
        session.add(task)
        session.commit()
        session.close()

        return task.id
