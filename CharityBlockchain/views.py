# -*- coding:utf-8 -*-
#encoding = utf-8
"""
Routes and views for the flask application.
"""

from flask import (
    Blueprint,flash,g,redirect,
    render_template,request,
    session,url_for
    )
from datetime import datetime
from CharityBlockchain.db import get_db
from CharityBlockchain.utils import createBlockChain
view = Blueprint('view',__name__,url_prefix='/view')
blockChain=createBlockChain()
@view.route('/<int:usertype>/<username>/info',methods=('GET','POST'))
def info(username,usertype):
    if request.method == 'POST':        
        user_rmb = float(request.form['rmb'])
        fund_project = request.form['sfound']
        error = None
        if usertype in (0,1,2,3):
            db = get_db()
            from_user = db.execute('SELECT * FROM user WHERE username = ?',
                (username,)).fetchone()
            project = db.execute('SELECT * FROM project WHERE name = ?',
                (fund_project,)).fetchone()
            if usertype == 2:
                to_user = db.execute('SELECT * FROM user WHERE username = ?',
                    ('0234',)).fetchone()
                db.execute('UPDATE project SET now_money = ? + ? WHERE id = ?',
                   (user_rmb,project['now_money'],project['id'],))
            elif usertype in (0,1):
                charge_person = request.form['sperson']
                to_user = db.execute('SELECT * FROM user WHERE username = ?',
                    (charge_person,)).fetchone()
            else:
                to_user = db.execute('SELECT * FROM user WHERE username = ?',
                    ('finish',)).fetchone()
                db.execute('UPDATE user SET account = account + ? WHERE id = ?',
                           (user_rmb,to_user['id'],))
            #TODO get hash
            hash=blockChain.doTrans(from_user['id'],to_user['id'],user_rmb)
            db.execute('''INSERT INTO deal (from_id,to_id,project_id,account,hash,tranDate)
            VALUES (?,?,?,?,?,?)''',(from_user['id'],to_user['id'],project['id'],user_rmb,hash,datetime.now().date()))
            db.commit()
        if not error:
            return render_template('view/finish.html')
        flash(error)
    elif request.method == 'GET' and request.args.get('viewfound') is not None:
        project_name = request.args.get('viewfound')
        db = get_db()
        project = db.execute('SELECT * FROM project WHERE name = ?',
                    (project_name,)).fetchone()
        project_deal = db.execute('SELECT * FROM deal WHERE project_id = ?',
            (project['id'],)).fetchall()
        return render_template('view/project.html',
                               project=project,
                               project_deal=project_deal,
                               year=datetime.now().year)
    db = get_db()
    project = db.execute('SELECT * FROM project').fetchall()
    person = db.execute('SELECT * FROM user WHERE account_type =1 or account_type =3').fetchall()
    return render_template('view/view.html',
        title=username,
        account_type=usertype,
        project=project,
        person=person,
        year=datetime.now().year,
        message = '区块链公益')