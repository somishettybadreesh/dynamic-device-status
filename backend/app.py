# app.py
from flask import Flask, send_from_directory
from blueprints.api import api
import os

def create_app():
    app = Flask(__name__, static_folder="../frontend", static_url_path="/")
    app.register_blueprint(api)

    @app.route('/')
    def index():
        return send_from_directory(app.static_folder, 'index.html')

    return app

if __name__ == "__main__":
    # optionally set FLASK_ENV=development in env if you want debug auto-reload
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
