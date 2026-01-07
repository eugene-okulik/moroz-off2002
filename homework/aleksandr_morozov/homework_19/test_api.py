import requests


def all_objects():
    response = requests.get('http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200, 'Status code is incorrect'
    assert (len(response.json()['data'])) == 18, 'Not all posts returned'


def one_object():
    object_id = new_object()
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{object_id}').json()
    assert response['id'] == object_id, 'Object not found'
    clear(object_id)


def post_an_object():
    body = {
        "data": {
            "color": "blue",
            "id": 123,
            "name": "colour",
            "size": None
        },
        "name": "NewPostman"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'NewPostman', 'The name is incorrect'


def new_object():
    body = {
        "data": {
            "color": "black",
            "id": 777,
            "name": "colour",
            "size": "great"
        },
        "name": "Newman"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    print(f'Создан объект с id {response.json()['id']}')
    return response.json()['id']


def clear(object_id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')
    print(f'Удален объект с id {object_id}')


def put_an_object():
    object_id = new_object()
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
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'NewPutman', 'The name is incorrect'
    clear(object_id)


def patch_an_object():
    object_id = new_object()
    body = {"name": "NewPatchman"}
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'NewPatchman', 'The name is incorrect'
    clear(object_id)


def delete_an_object():
    object_id = new_object()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')
    assert response.text == f'Object with id {object_id} successfully deleted', 'Incorrect body response'
    assert response.status_code == 200, 'Status code is incorrect'


# one_object()
patch_an_object()
