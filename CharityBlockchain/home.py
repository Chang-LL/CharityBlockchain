from flask import (
    Blueprint,flash,g,redirect,
    render_template,request,
    session,url_for
    )
from datetime import datetime
homepage=Blueprint('home',__name__,url_prefix='/home')

@homepage.route('/')
@homepage.route('/home')
def home():
    """Renders the home page."""
    return render_template('index.html',
        title='Home Page',
        year=datetime.now().year,)

@homepage.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template('home/contact.html',
        title='联系我们',
        year=datetime.now().year,
        message='联系页面')

@homepage.route('/about')
def about():
    """Renders the about page."""
    return render_template('home/about.html',
        title='关于',
        year=datetime.now().year,
        message='区块链公益')
