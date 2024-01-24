import pytest
from sqlmodel import Session
from task_manager.db import DB
from task_manager.model import Tasks, TaskStatus


@pytest.fixture
def task1():
    """
    Create a Task 1
    """
    task1 = Tasks(
        title="Go to the Gym",
        description="Visit Gym at 09:00",
        status=TaskStatus.NOT_STARTED,
    )
    yield task1


@pytest.fixture
def task2():
    """
    Create a Task 2
    """
    task2 = Tasks(
        title="Buy Groceries",
        description="Large shopping list - buy at 12:00",
        status=TaskStatus.NOT_STARTED,
    )
    yield task2


@pytest.fixture
def db_instance(scope="session"):
    """
    Create a DB Instance
    """
    db = DB()
    yield db


@pytest.fixture
def session(db_instance, scope="session"):
    """
    Create a Session, close after test session, uses `db_instance` fixture
    """
    session = Session(db_instance.engine)
    yield session
    session.close()


@pytest.fixture
def db_instance_empty(db_instance, session, scope="function"):
    """
    Create an Empty DB Instance, uses `db_instance` and `session` fixtures
    """
    # Clear DB before test function
    db_instance.delete_all_tasks(session=session)
    yield db_instance

    # Clear DB after test function
    db_instance.delete_all_tasks(session=session)
