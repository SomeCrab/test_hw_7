from dotenv import load_dotenv
from os import getenv
from uritools import uricompose

# creds
load_dotenv()
CREDENTIALS = {
    "username": getenv('USERNAME'),
    "password": getenv('PASSWORD')
}

# base url
SCHEME = 'http'
DOMAIN = '5.101.50.27'
PORT = '8000'
BASE_URL = uricompose(scheme=SCHEME, host=DOMAIN, port=PORT)

# wipe path
WIPE_PATH = '/magic/delete_create_all'

# login
LOGIN_PATH = '/auth/login'

# employee path
EMPLOYEE_PATH = '/employee'
EMP_CREATE_PATH = f'{EMPLOYEE_PATH}/create'
EMP_INFO_PATH = f'{EMPLOYEE_PATH}/info/'
EMP_CHANGE_PATH = f'{EMPLOYEE_PATH}/change/'

# expected employee data
FIRST_ID = 1
DEFAULT_STATE_NOT_EXISTING_ID = 7
EMPLOYEE_DATA = {
        "first_name": "Stanley",
        "last_name": "Tweedle",
        "middle_name": "Captain",
        "company_id": 1,
        "email": "PowerfulStanley@ostral-b-heretics.com",
        "phone": "+790987654321",
        "birthdate": "1944-10-31",
        "is_active": True
    }
EMPLOYEE_DATA_CHANGE = {
        "first_name": "Stanley",
        "last_name": "Tweedle-Arch-Traitor",
        "middle_name": "Captain",
        "company_id": 1,
        "email": "ArchTraitorStanley@ostral-b-heretics.com",
        "phone": "Not present",
        "birthdate": "1944-10-31",
        "is_active": False
    }
DEFAULT_FIRST_EMPLOYEE = {
    "id": 1,
    "first_name": "Иван",
    "last_name": "Иванов",
    "middle_name": "Иванович",
    "company_id": 1,
    "email": "ivan@example.com",
    "phone": "+79001234567",
    "birthdate": "1990-01-01",
    "is_active": True
    }

# expected codes
EXPECTED_200 = 200
EXPECTED_201 = 201