from flask import current_app
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from rest_api.apps.todo_list.repositories import ListRepository
from rest_api.database import Base


class TaskRepository(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    finished = Column(Boolean)
    list_id = Column(Integer, ForeignKey(ListRepository.id))

    @classmethod
    def create_task(cls, name, description, list_id):
        task_object = TaskRepository(name=name, description=description, finished=False, list_id=list_id)
        current_app.db_session.add(task_object)
        current_app.db_session.commit()
        return task_object.id

    @classmethod
    def get_all_task_from_list(self, list_id):
        tasks_pid = current_app.db_session.query(TaskRepository).filter_by(list_id=list_id)
        tasks = current_app.db_session.execute(tasks_pid)
        return tasks

    @classmethod
    def delete_task(cls, task_id):
        task = current_app.db_session.query(TaskRepository).filter_by(id=task_id).first()
        current_app.db_session.delete(task)
        current_app.db_session.commit()
        return task_id

    @classmethod
    def edit_task(cls, task_id, **kwargs):
        task_object = current_app.db_session.query(TaskRepository).filter_by(id=task_id).first()
        for field_name, field_value in kwargs.items():
            setattr(task_object, field_name, field_value)
        current_app.db_session.add(task_object)
        current_app.db_session.commit()
        return True


