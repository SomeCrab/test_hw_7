import requests
from uritools import urijoin
from config import (
    LOGIN_PATH,
    EMP_INFO_PATH,
    EMP_CREATE_PATH,
    EMP_CHANGE_PATH,
    WIPE_PATH,
    CREDENTIALS,
    EXPECTED_200,
    EXPECTED_201,
    )

class EmployeeApi():
    """Employee API class"""

    def __init__(self, url: str) -> None:
        """Init base url field"""
        self.url = url


    def __expectation_failure_msg(self, actual_code: int, expected_code: int) -> str:
        """Returns failure message for unexpected codes"""
        return f"\nExpected code: {expected_code}\nActual code: {actual_code}"


    def __assert_response_code(self, actual_code, expected_code) -> None:
        #response.raise_for_status()
        assert expected_code == actual_code, self.__expectation_failure_msg(actual_code, expected_code)


    def get_employee(self, employee_id: int) -> dict:
        """Sends GET request to get info ybout employee by provided ID."""
        info_url = urijoin(self.url, EMP_INFO_PATH)
        info_id_url = urijoin(info_url, str(employee_id))
        response = requests.get(info_id_url)

        self.__assert_response_code(response.status_code, EXPECTED_200)
        return response.json()


    def create_employee(self, employee_data: dict) -> dict:
        """Sends POST request to create employee using provided data."""
        create_url = urijoin(self.url, EMP_CREATE_PATH)
        response = requests.post(create_url, json=employee_data)

        self.__assert_response_code(response.status_code, EXPECTED_200)
        return response.json()


    def get_token(self) -> str:
        """Sends POST request to get tocken and returns it."""
        login_url = urijoin(self.url, LOGIN_PATH)
        response = requests.post(login_url, json=CREDENTIALS)

        self.__assert_response_code(response.status_code, EXPECTED_200)
        return response.json()["user_token"]


    def change_employee(self, id: int, employee_data: dict) -> dict:
        """Sends PATCH request to change employee values using provided data"""
        token = self.get_token()
        change_url = urijoin(self.url, EMP_CHANGE_PATH)
        change_id_url = urijoin(change_url, str(id))
        response = requests.patch(change_id_url, params={'client_token': token}, json=employee_data)
        #print(f"{change_id_url}?client_token={token}")

        self.__assert_response_code(response.status_code, EXPECTED_200)
        return response.json()


    def delete_and_recreate_all_employees(self) -> dict:
        """Sends GET request to wipe whole DB and create default testing data."""
        token = self.get_token()
        wipe_url = urijoin(self.url, WIPE_PATH)
        response = requests.get(wipe_url, params={'client_token': token})

        self.__assert_response_code(response.status_code, EXPECTED_200)
        return response.json()
