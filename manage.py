from rest_api.app import setup_app
from rest_api.config import DebugConfig, ProductionConfig

app = setup_app(config=ProductionConfig)


if __name__ == "__main__":
    app = setup_app(config=DebugConfig)
    app.run(host="localhost", port=5000)
