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
view = Blueprint('view',__name__,url_prefix='/view')

@view.route('/<username>/info',methods=('GET','POST'))
def info(username):
    if request.method == 'POST':
        userrmb=request.form['rmb']
        userfound=request.form['sfound']
        print(userfound,userrmb)
    return render_template('view/view.html',
        title=username,
        year=datetime.now().year,
        message='区块链公益')

