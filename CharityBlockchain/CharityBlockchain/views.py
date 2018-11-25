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

from web3 import Web3, HTTPProvider
from web3.eth import Eth
from web3.utils.encoding import to_text, to_hex

#connect to blockchain and get account info
web3 = Web3(HTTPProvider('http://localhost:8545'))
eth = Eth(web3)
block_account = web3.eth.accounts


view = Blueprint('view',__name__,url_prefix='/view')

@view.route('/<int:usertype>/<username>/info',methods=('GET','POST'))
def info(username,usertype):
    #user donate money

    if request.method == 'POST':        
        user_rmb = request.form['rmb']
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
                    ('1234',)).fetchone()
            elif usertype in (0,1):
                charge_person = request.form['sperson']
                to_user = db.execute('SELECT * FROM user WHERE username = ?',
                    (charge_person,)).fetchone()
            else:
                to_user = db.execute('SELECT * FROM user WHERE username = ?',
                    ('finish',)).fetchone()
            #TODO get hash
            #hash=gethash()
            hash = None
            db.execute('''INSERT INTO deal (from_id,to_id,project_id,account,hash,tranDate)
            VALUES (?,?,?,?,?,?)''',(from_user['id'],to_user['id'],project['id'],user_rmb,hash,datetime.now()))
        if not error:
            return render_template('view/finish.html')
        flash(error)
    elif request.method == 'GET' and request.args.get('viewfound') is not None:
        project_name = request.args.get('viewfound')
        db = get_db()
        project = db.execute('SELECT * FROM project WHERE name = ?',
                    (project_name,)).fetchone()
        project_deal = db.execute('SELECT * FROM deal WHERE project_id = ?',
            (project['id'],)).fetchone()
        return render_template('view/project.html',
                               project=project,
                               project_deal=project_deal,
                               year=datetime.now().year)
    
    return render_template('view/view.html',
        title=username,
        account_type=usertype,
        year=datetime.now().year,
        message='区块链公益')

def doTrans(account1, account2, money, tex):
    baccount1 = account_s(account1)
    baccount2 = account_s(account2)

    payload = {
        'from':block_account[baccount1],
        'to':block_account[baccount2],
        'value':money,
        'data':to_hex(str.encode(tex))
        }
    hash = web3.eth.sendTransaction(payload)
    web3.eth.waitForTransactionReceipt(tx_hash)
    return hash

def getTrans(hash):
    payload = web3.eth.getTransection(hash)
    payload.input=to_tex(payload.input)
    return payload

def account_s(account):
    baccount = 11
    return baccount
