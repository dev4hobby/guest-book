from os import getenv, environ
from utils.env import init_json_env
from datetime import datetime

init_json_env(environ.get("ENVIRONMENT", "dev"))
WOKEUP_TIME = datetime.now()
DATABASE = {
    "host": getenv("MONGO_HOST"),
    "port": getenv("MONGO_PORT", 27017),
    "user": getenv("MONGO_USER"),
    "password": getenv("MONGO_PASSWORD"),
    "name": getenv("MONGO_NAME"),
}

MAX_COMMENT_LENGTH = getenv("MAX_COMMENT_LENGTH", 10)
