
class DebugConfig:
    DEBUG = True
    DB_URI = "sqlite:///./db.sqlite"


class ProductionConfig:
    DEBUG = False
    DB_URI = "sqlite:///./db.sqlite"
