from flask import render_template, Blueprint, session, request, jsonify, redirect

# Home_Page blueprint definition
homePage = Blueprint(
    'homePage',
    __name__,
    static_folder='static',
    static_url_path='/homePage',
    template_folder='templates'
)

@homePage.route('/')
@homePage.route('/homePage')
def index():
    return render_template('homePage.html')

# Routes
#@homepage.route('/homepage')
#@homepage.route('/home')
#@homepage.route('/')
#def index():
 #   return render_template('Home_Page.html')

# @homepage.route('/homepage')
# @homepage.route('/home')
# @homepage.route('/')
# def redirect_homepage():
    # print('I am in /Homepage route!')
  #  return redirect(url_for('homepage.index'))
