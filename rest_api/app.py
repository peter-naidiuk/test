from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .database import Base
from .utils.base_view import BaseView


def _setup_handling_exceptions(application):

    @application.errorhandler(Exception)
    def handle_exception(e):
        if not hasattr(e, "status"):
            status = 500
        else:
            status = e.status
        return BaseView.get_response(data=str(e), status=status)


def _setup_blueprints(application):
    from .apps import APPS
    for app in APPS:
        application.register_blueprint(app, url_prefix=app.url_prefix)


def _setup_db(application, db_uri):
    engine = create_engine(db_uri)
    from .apps.todo_task.repositories import TaskRepository
    from .apps.todo_list.repositories import ListRepository
    Base.metadata.create_all(engine)

    @application.before_request
    def create_db_session():
        Session = sessionmaker(bind=engine)
        application.db_session = Session()


def setup_app(config):
    application = Flask(__name__)
    application.config.from_object(config)
    _setup_db(application, config.DB_URI)
    _setup_blueprints(application)
    _setup_handling_exceptions(application)
    return application






