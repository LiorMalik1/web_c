from flask import render_template, Blueprint, session, request, jsonify, redirect
from db_connector import *

# About_Us blueprint definition
searchResults = Blueprint(
    'searchResults',
    __name__,
    static_folder='static',
    static_url_path='/searchResults',
    template_folder='templates'
)

# Routes
@searchResults.route('/searchResults')
def index():
    return render_template('searchResults.html')

@searchResults.route('/searchResults')
def show_results():
    username = session['username']
    customer = get_customer_by_username(username)
    city = customer['city']
    business = get_business_by_city(city)
    return render_template('searchResults.html', city=city, business=business)