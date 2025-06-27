from api.employee_api import EmployeeApi
import pytest
from config import (
    BASE_URL,
    EMPLOYEE_DATA,
    DEFAULT_FIRST_EMPLOYEE,
    EMPLOYEE_DATA_CHANGE,
    FIRST_ID,
    DEFAULT_STATE_NOT_EXISTING_ID,
    )


def test_get_employee():
    """Testing /info endpoint
        - Creates new user
        - Gets new user
        - Checks if the user gets as expected
    """
    api = EmployeeApi(BASE_URL)

    new_employee = api.create_employee(EMPLOYEE_DATA)

    actually_employee = api.get_employee(new_employee['id'])

    EMPLOYEE_DATA.update({"id": new_employee['id']})
    expected_employee = EMPLOYEE_DATA

    assert actually_employee == expected_employee, f"\nExpected: '{expected_employee}'\nGot: '{actually_employee}'"


def test_create_employee():
    """Testing /create endpoint
        - Creates new user
        - Checks if the user creates as expected
    """
    api = EmployeeApi(BASE_URL)

    actually_employee = api.create_employee(EMPLOYEE_DATA)
    
    EMPLOYEE_DATA.update({"id": actually_employee['id']})
    expected_employee = EMPLOYEE_DATA

    assert actually_employee == expected_employee, f"\nExpected: '{expected_employee}'\nGot: '{actually_employee}'"


def test_change_employee():
    """Testing /change endpoint
        - Creates new user
        - Changes its data to data from config
        - Checks if the data changes as expected
    """
    api = EmployeeApi(BASE_URL)

    new_employee = api.create_employee(EMPLOYEE_DATA)

    actually_employee = api.change_employee(new_employee['id'], EMPLOYEE_DATA_CHANGE)

    EMPLOYEE_DATA_CHANGE.update({"id": new_employee['id']})
    expected_employee = EMPLOYEE_DATA_CHANGE

    assert actually_employee == expected_employee, f"\nExpected: '{expected_employee}'\nGot: '{actually_employee}'"


def test_delete_and_recreate_all_employees():
    """Testing /magic/delete_create_all endpoint.
        - Changes first default user
        - Wipes DB and puts default data to it
        - Checks if first default user is default enought
        - Checks if first default non-existant user is is not existing
    """
    api = EmployeeApi(BASE_URL)

    api.change_employee(FIRST_ID, EMPLOYEE_DATA_CHANGE)

    api.delete_and_recreate_all_employees()

    actually_first_employee = api.get_employee(FIRST_ID)
    assert actually_first_employee == DEFAULT_FIRST_EMPLOYEE, f"\nExpected: '{DEFAULT_FIRST_EMPLOYEE}'\nGot: '{actually_first_employee}'"

    assert_error = False
    try:
        api.get_employee(DEFAULT_STATE_NOT_EXISTING_ID)
    except AssertionError:
        assert_error = True
    
    if not assert_error:
        pytest.fail(f'User with id "{DEFAULT_STATE_NOT_EXISTING_ID}" exists, he better dont next time...')
