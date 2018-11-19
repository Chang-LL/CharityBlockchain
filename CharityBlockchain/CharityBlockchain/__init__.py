"""
The flask application package.
"""
import os
from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY='qetasg',#TODO
            DATABASE=os.path.join(app.instance_path,'CharityBlockchain.sqlite'))
    from CharityBlockchain import db
    db.init_app(app)
    from CharityBlockchain import user
    app.register_blueprint(user.user)
    import CharityBlockchain.views
    from datetime import datetime
    from flask import render_template
    #from CharityBlockchain import app

    @app.route('/')
    @app.route('/home')
    def home():
        """Renders the home page."""
        return render_template('index.html',
            title='Home Page',
            year=datetime.now().year,)

    @app.route('/contact')
    def contact():
        """Renders the contact page."""
        return render_template('contact.html',
            title='联系我们',
            year=datetime.now().year,
            message='联系页面')

    @app.route('/about')
    def about():
        """Renders the about page."""
        return render_template('about.html',
            title='关于',
            year=datetime.now().year,
            message='区块链公益')

    @app.route('/sign_in')
    def sign_in():
        """Sign in the System"""
        return render_template('sign_in.html',
            tilte='登录',
            year=datetime.now().year)

    @app.route('/sign_up')
    def sign_up():
        """Sign up the System"""
        return render_template('sign_up.html',
            tilte='注册',
            year=datetime.now().year)
    return app
