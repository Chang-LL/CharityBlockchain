"""
The flask application package.
"""
import os
from flask import Flask,redirect,url_for
def create_app():
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY='qetasg',#TODO
            DATABASE=os.path.join(app.instance_path,'CharityBlockchain.sqlite'))
    from CharityBlockchain import db
    db.init_app(app)
    from CharityBlockchain import user
    app.register_blueprint(user.user)
    from CharityBlockchain import home
    app.register_blueprint(home.homepage)
    from CharityBlockchain import views
    app.register_blueprint(views.view)
    @app.route('/')
    def Home():
        return redirect(url_for('home.home'))
    return app
