from flask import current_app
from sqlalchemy import Column, Integer, String

from rest_api.database import Base


class ListRepository(Base):
    __tablename__ = 'lists'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    @classmethod
    def create_list(cls, name):
        list_object = ListRepository(name=name)
        current_app.db_session.add(list_object)
        current_app.db_session.commit()
        return list_object.id

    @classmethod
    def get_all_lists(cls):
        data = current_app.db_session.query(ListRepository).all()
        return data

    @classmethod
    def get_list_by_id(cls, list_id):
        data = current_app.db_session.query(ListRepository).filter_by(id=list_id).first()
        return data
