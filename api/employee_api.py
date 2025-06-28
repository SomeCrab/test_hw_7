import requests
from config import (
    LOGIN_URL,
    EMP_INFO_URL,
    EMP_CREATE_URL,
    EMP_CHANGE_URL,
    WIPE_URL,
    CREDENTIALS,
    EXPECTED_200,
    EXPECTED_201,
    )

class EmployeeApi():
    """Employee API class"""

    def __init__(self, url):
        """Init base url field"""
        self.url = url


    def __expectation_failure_msg(self, actual_code, expected_code) -> str:
        """Returns failure message for unexpected codes"""
        return f"\nExpected code: {expected_code}\nActual code: {actual_code}"


    def __assert_response_code(self, actual_code, expected_code):
        #response.raise_for_status()
        assert expected_code == actual_code, self.__expectation_failure_msg(actual_code, expected_code)


    def get_employee(self, employee_id):
        """Sends GET request to get info ybout employee by provided ID."""
        response = requests.get(f"{self.url}{EMP_INFO_URL}{employee_id}")

        self.__assert_response_code(response.status_code, EXPECTED_200)
        return response.json()


    def create_employee(self, employee_data):
        """Sends POST request to create employee using provided data."""
        response = requests.post(f"{self.url}{EMP_CREATE_URL}", json=employee_data)

        self.__assert_response_code(response.status_code, EXPECTED_200)
        return response.json()


    def get_token_parameter(self) -> str:
        """Sends POST request to get tocken and returns it as a tocken parameter for requests"""

        response = requests.post(f"{self.url}{LOGIN_URL}", json=CREDENTIALS)

        self.__assert_response_code(response.status_code, EXPECTED_200)
        return f'?client_token={response.json()["user_token"]}'


    def change_employee(self, id, employee_data):
        """Sends PATCH request to change employee values using provided data"""
        tocken_parameter = self.get_token_parameter()
        response = requests.patch(f"{self.url}{EMP_CHANGE_URL}{id}{tocken_parameter}", json=employee_data)
        #print(f"{self.url}{EMP_CHANGE_URL}{id}?client_token={tocken_parameter}")

        self.__assert_response_code(response.status_code, EXPECTED_200)
        return response.json()


    def delete_and_recreate_all_employees(self):
        """Sends GET request to wipe whole DB and create default testing data."""
        tocken_parameter = self.get_token_parameter()

        response = requests.get(f"{self.url}{WIPE_URL}{tocken_parameter}")

        self.__assert_response_code(response.status_code, EXPECTED_200)
        return response.json()
