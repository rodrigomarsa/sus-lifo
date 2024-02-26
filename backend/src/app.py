from flask import Flask
from flask_cors import CORS
from database.db import db
from controllers.user_controller import user_controller
from os import environ
from waitress import serve

app = Flask(__name__)
CORS(app)

URI = "mysql+pymysql://root:password@localhost/sus_lifo_database"
app.config["SQLALCHEMY_DATABASE_URI"] = URI

db.init_app(app)

app.register_blueprint(user_controller, url_prefix="/")


def start_server(host="0.0.0.0", port=8000):
    if environ.get("FLASK_ENV") != "production":
        return app.run(debug=True, host=host, port=port)
    else:
        serve(app, host=host, port=port)


if __name__ == "__main__":
    start_server()
