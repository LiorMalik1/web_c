import os
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://malno:noamal2210@noa.ghwa7bo.mongodb.net/?retryWrites=true&w=majority&appName=noa"

# create cluster
client = MongoClient(uri, server_api=ServerApi('1'))

# get all dbs and collections that needed
DB = client['fixItDB']
customers_col = DB['customers']
business_col = DB['business']

# add here bkababkabk
# add hrewrererfefnjk



def get_business_by_username(username):
    return business_col.find_one({'username': username})

def get_business():
    return list(business_col.find())

def get_business_by_city(city):
    return business_col.find({'city': city})

def create_business(businessName, username, email, password, city ,gender, phone, proffesion, seniority):
    new_business = {
        'businessName': businessName,
        'username': username,
        'email': email,
        'password': password,
        'city': city,
        'gender': gender,
        'phone': phone,
        'proffesion': proffesion,
        'seniority': seniority,
        'numOfClicks': 0
        #'leftClasses':0,
        #'classes': []
    }
    business_col.insert_one(new_business)

##customers collection functions
##customers exists
def check_if_registered(username):
    if get_customer_by_username(username):
        return True
    return False

def get_customer_by_username(username):
    return customers_col.find_one({'username': username})

def get_customers():
    return list(customers_col.find())

def create_customer(firstName,lastName, username, email, password, city,gender, phone):
    new_customer = {
        'firstName': firstName,
        'lastName' : lastName,
        'username': username,
        'email': email,
        'password': password,
        'city' : city,
        'gender' : gender,
        'phone': phone
    }
    customers_col.insert_one(new_customer)


