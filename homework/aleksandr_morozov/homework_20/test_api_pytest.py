import requests
import pytest


@pytest.fixture(scope='session')
def start():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(autouse=True)
def every_test():
    print('before test')
    yield
    print('after test')

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
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')
    print('Удален объект с id: ', object_id)


@pytest.mark.medium
def test_get_all(start):
    response = requests.get('http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200, 'Status code is incorrect'
    assert (len(response.json()['data'])) > 1, 'Not all objects returned'


def test_get_one(new_object):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_object}').json()
    assert response['id'] == new_object, 'Object not found'


@pytest.mark.parametrize('name', ['ONE MAN','twoMan', '123_man'])
def test_post_object(name):
    body = {
        "data": {
            "color": "blue",
            "id": 123,
            "name": "colour",
            "size": None
        },
        "name": name
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == name, 'The name is incorrect'


@pytest.mark.critical
def test_put_object(new_object):
    body = {
        "data": {
            "color": "green",
            "id": 111,
            "name": "colour",
            "size": "well"
        },
        "name": "NewPutman"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_object}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'NewPutman', 'The name is incorrect'


def test_patch_object(new_object):
    body = {"name": "NewPatchman"}
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{new_object}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'NewPatchman', 'The name is incorrect'


def test_delete_object(new_object):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_object}')
    assert response.text == f'Object with id {new_object} successfully deleted', 'Incorrect body response'
    assert response.status_code == 200, 'Status code is incorrect'
