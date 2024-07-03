from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from apps.config import config

db = SQLAlchemy()
csrf = CSRFProtect()


def create_app(config_key):
    app = Flask(__name__)
    app.config.from_object(config[config_key])

    db.init_app(app)
    Migrate(app, db)
    csrf.init_app(app)

    from apps.main import views as main_views

    app.register_blueprint(main_views.main, url_prefix="/main")

    # from apps.sub import views as sub_views

    # app.register_blueprint(sub_views.sub, url_prefix="/sub")

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template("main/404.html"), 404

    return app
