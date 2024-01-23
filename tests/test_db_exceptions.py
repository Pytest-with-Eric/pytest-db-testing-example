import pytest
import sqlalchemy
from task_manager.model import TaskStatus
from task_manager.exceptions import TaskNotFoundError


def test_read_task_not_found(db_instance_empty, session, task1, task2):
    """
    Test the reading of a task that does not exist
    """
    # Write 2 Tasks to DB
    db_instance_empty.create_task(task=task1, session=session)
    db_instance_empty.create_task(task=task2, session=session)

    # Search for Task with ID 100
    with pytest.raises(TaskNotFoundError):
        db_instance_empty.read_task(task_id=100, session=session)


def test_update_task_not_found(db_instance_empty, session, task1, task2):
    """
    Test the updating of a task that does not exist
    """
    # Write 2 Tasks to DB
    db_instance_empty.create_task(task=task1, session=session)
    db_instance_empty.create_task(task=task2, session=session)

    # Update Task with ID 100
    with pytest.raises(TaskNotFoundError):
        db_instance_empty.update_task(
            session=session,
            task_id=100,
            task_status=TaskStatus.COMPLETED,
        )


def test_delete_task_not_found(db_instance_empty, session, task1, task2):
    """
    Test the deletion of a task that does not exist
    """
    # Write 2 Tasks to DB
    db_instance_empty.create_task(task=task1, session=session)
    db_instance_empty.create_task(task=task2, session=session)

    # Delete Task with ID 100
    with pytest.raises(TaskNotFoundError):
        db_instance_empty.delete_task(session=session, task_id=100)


def test_write_invalid_task(db_instance, session, task1):
    """
    Test the Tasks Model with invalid data
    """
    # Update task1 with Invalid Data
    task1.id = "test"
    task1.status = "test"

    # Write Task to DB and expect an IntegrityError
    with pytest.raises(
        sqlalchemy.exc.IntegrityError
    ):  # Incorrect Data Types for ID and Status raises IntegrityError
        db_instance.create_task(task=task1, session=session)
