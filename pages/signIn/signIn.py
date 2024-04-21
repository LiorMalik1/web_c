from flask import render_template, Blueprint, session, request, jsonify, redirect, url_for
import db_connector
from db_connector import *
#check here
# About_Us blueprint definition
signIn = Blueprint(
    'signIn',
    __name__,
    static_folder='static',
    static_url_path='/signIn',
    template_folder='templates'
)

# Routes
@signIn.route('/signIn')
def index():
    return render_template('signIn.html')

@signIn.route('/signIn', methods=['POST'])
def signInCustomer():
    username = request.form.get('username')
    if not check_if_registered(username):
        create_customer(request.form.get('firstName'),
                        request.form.get('lastName'),
                        request.form.get('username'),
                        request.form.get('email'),
                        request.form.get('password'),
                        request.form.get('city'),
                        request.form.get('gender'),
                        request.form.get('phone')
                        )
        print("create_customer")
        return redirect(url_for('signIn.index'))
    else:
        message = "Username already exists in the system, please choose another username"
        return render_template('signIn.html', msg1=message)
    return render_template('signIn.html', msg1='')