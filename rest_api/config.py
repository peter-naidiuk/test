
class DebugConfig:
    DEBUG = True
    DB_URI = "sqlite:///db"


class ProductionConfig:
    DEBUG = False
    DB_URI = "sqlite:///db"
