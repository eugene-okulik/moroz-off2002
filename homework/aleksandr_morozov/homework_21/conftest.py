import requests
import pytest
import allure


@allure.title('Creating session data')
@pytest.fixture(scope='session')
def start():
    print('Start testing')
    yield
    with allure.step('Cleaning session data'):
        print('Testing completed')


@allure.title('Each test preparing')
@pytest.fixture(autouse=True)
def every_test():
    print('before test')
    yield
    with allure.step('Each test cleaning'):
        print('after test')


@allure.title('Creating test object')
@pytest.fixture()
def new_object():
    body = {
        "data": {"color": "black", "id": 777, "name": "colour", "size": "great"},
        "name": "Newman"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    ).json()
    object_id = response['id']
    print('Создан объект с id: ', object_id)
    yield response['id']
    with allure.step('Deleting test object'):
        requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')
        print('Удален объект с id: ', object_id)
