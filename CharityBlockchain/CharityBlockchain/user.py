import functools

from flask import (
    Blueprint,flash,g,redirect,
    render_template,request,
    session,url_for
    )
from werkzeug.security import(
    check_password_hash,
    generate_password_hash
    )
from CharityBlockchain.db import get_db

user=Blueprint('user',__name__,url_prefix='/user')

@user.route('/register',methods=('GET','POST'))
def register():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        db=get_db()
        error=None
        if not username:
            error="请输入用户名!"
        elif not password:
            error="请输入密码!"
        elif db.execute('SELECT id FROM user WHERE username = ?',
            (username,)).fetchone() is not None:
            error = f'用户名 {username} 已存在!'
        if error is None:
            db.execute('INSERT INTO user (username,password) VALUES (?,?)',
                (username,generate_password_hash(password)))
            db.commit()
            return redirect(url_for('user.login'))
        flash(error)
    return render_template('user/register.html')

@user.route('/login',methods=('GET','POST'))
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute('SELECT * FROM user WHERE username =?',
            (username,)).fetchone()

        if user is None:
            error = '用户名或密码错误'
        elif not check_password_hash(user['password'],password):
            error = '用户名或密码错误'
        
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('logintodo'))
        flash(error)

    return render_template('user/login.html')
@user.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute('SELECT * FROM user WHERE id = ?',
            (user_id,)).fetchone()

@user.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('user.login'))
        return view(**kwargs)
    return wrapped_view