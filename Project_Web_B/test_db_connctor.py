import pytest
from mongodb_client_factory import MongodbClientFactory
import db_connector


business_dto = {
    'businessName': "bla",
    'username': "bla_yarden",
    'email': "yarden@email",
    'password': "XXXXXx",
    'city': "tel aviv",
    'gender': "mevn",
    'phone': "045324325r2353",
    'proffesion': "proffesion",
    'seniority': "dsgds",
}
def test_db_connection():
    client = MongodbClientFactory().get_instance()
    client.admin.command('ping')

def test_create_business(business_dto):
    db_connector.create_business("bla", "bla_yarden","email", "city", "gev", "g","r3253525", "p", "s")

