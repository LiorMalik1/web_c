from flask import render_template, Blueprint, session, request, jsonify, redirect
from db_connector import *

# About_Us blueprint definition
logIn = Blueprint(
    'logIn',
    __name__,
    static_folder='static',
    static_url_path='/logIn',
    template_folder='templates'
)

# Routes
@logIn.route('/logIn')
def index():
    return render_template('logIn.html')

@logIn.route('/logIn', methods = ['POST'])
def logIn_user():
    username = request.form.get('username')
    if check_if_registered(username):
        customer = get_customer_by_username(request.form.get('username'))
        city = customer.city
        if customer['password'] == request.form.get('password'):
            session['username'] = request.form.get('username')
            session['logged_in'] = True
            return render_template('homePage.html', customer=customer)
        else:
            msg1 = 'Incorrect password, please try again'
            return render_template("signIn.html", msg1=msg1)
    else:
        msg1 = 'Username does not exist, please try again'
        return render_template("signIn.html", msg1=msg1)
    return render_template("signIn.html", msg1="")