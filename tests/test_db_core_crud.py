import pytest
from task_manager.model import TaskStatus
from task_manager.exceptions import TaskNotFoundError


def test_create_and_read_task(db_instance_empty, session, task1):
    """
    Test the creation and reading of a task
    """
    # Write Task to DB
    db_instance_empty.create_task(task=task1, session=session)

    # # Read Task from DB
    task = db_instance_empty.read_task(task_id=1, session=session)
    assert task.title == task1.title
    assert task.description == task1.description
    assert task.status == task1.status


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


def test_update_task_taskstatus(db_instance_empty, session, task1):
    """
    Test the updating of a task (TaskStatus)
    """
    # Write Task to DB
    db_instance_empty.create_task(task=task1, session=session)

    # Update Task
    db_instance_empty.update_task(
        session=session,
        task_id=1,
        task_status=TaskStatus.COMPLETED,
    )

    # Read Task from DB
    task = db_instance_empty.read_task(task_id=1, session=session)

    # Check Task Status and Updated At
    assert task.status == TaskStatus.COMPLETED
    assert task.updated_at > task.created_at


def test_update_task_tasktitle(db_instance_empty, session, task1):
    """
    Test the updating of a task (TaskTitle)
    """
    # Write Task to DB
    db_instance_empty.create_task(task=task1, session=session)

    # Update Task
    db_instance_empty.update_task(
        session=session,
        task_id=1,
        task_title="New Title",
    )

    # Read Task from DB
    task = db_instance_empty.read_task(task_id=1, session=session)

    # Check Task Title and Updated At
    assert task.title == "New Title"
    assert task.updated_at > task.created_at


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


def test_delete_task(db_instance_empty, session, task1, task2):
    """
    Test the deletion of a task
    """
    # Write 2 Tasks to DB
    db_instance_empty.create_task(task=task1, session=session)
    db_instance_empty.create_task(task=task2, session=session)

    # Delete Task
    db_instance_empty.delete_task(session=session, task_id=1)

    # Read Task from DB
    with pytest.raises(TaskNotFoundError):
        db_instance_empty.read_task(task_id=1, session=session)


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


def test_read_all_tasks(db_instance_empty, session, task1, task2):
    """
    Test the reading of all tasks
    """
    # Write 2 Tasks to DB
    db_instance_empty.create_task(task=task1, session=session)
    db_instance_empty.create_task(task=task2, session=session)

    # Read all Tasks from DB
    tasks = db_instance_empty.read_tasks(session=session)
    assert len(tasks) == 2
    assert tasks[0].title == task1.title
    assert tasks[1].title == task2.title


def test_read_all_tasks_empty(db_instance_empty, session):
    """
    Test the reading of all tasks when the DB is empty
    """
    # Read all Tasks from DB
    tasks = db_instance_empty.read_tasks(session=session)
    assert len(tasks) == 0


def test_delete_all_tasks(db_instance_empty, session, task1, task2):
    """
    Test the deletion of all tasks
    """
    # Write 2 Tasks to DB
    db_instance_empty.create_task(task=task1, session=session)
    db_instance_empty.create_task(task=task2, session=session)

    # Delete all Tasks from DB
    db_instance_empty.delete_all_tasks(session=session)

    # Read all Tasks from DB
    tasks = db_instance_empty.read_tasks(session=session)
    assert len(tasks) == 0
