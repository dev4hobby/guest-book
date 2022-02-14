def create_app():
    from flask import Flask, make_response, jsonify
    from flask_cors import CORS
    from utils.env import get_database_uri, generate_key
    from settings import DATABASE
    from core.database import db
    from . import home, misc, comment

    app = Flask(__name__)
    app.secret_key = generate_key(16)
    app.config["MONGODB_SETTINGS"] = {
        "db": DATABASE.get("name"),
        "host": get_database_uri(DATABASE),
        "port": int(DATABASE.get("port")),
        "username": DATABASE.get("username"),
        "password": DATABASE.get("password"),
    }
    db.init_app(app)

    @app.errorhandler(404)
    def resource_not_found(e):
        return make_response(jsonify(error="Not found!"), 404)

    app.register_blueprint(home.home)
    app.register_blueprint(misc.misc)
    app.register_blueprint(comment.comment)

    CORS(app, resources={r"/*": {"origins": "*"}}, support_credentials=True)

    return app
