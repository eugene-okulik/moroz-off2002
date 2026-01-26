import requests
import pytest
import allure


@allure.feature('API')
@allure.story('Получение объектов')
@allure.title('GET /object - получение списка всех объектов')
@allure.issue('https://ru.ruwiki.ru/wiki/Авиация_эфиопо-эритрейского_конфликта','SCP-111. Подготовка API ч.1')
@allure.id('T1001')
@pytest.mark.medium
def test_get_all(start):
    with allure.step('Вызов метода по REST'):
        response = requests.get('http://objapi.course.qa-practice.com/object')
    with allure.step('Проверка что статус ответа 200'):
        assert response.status_code == 200, 'Status code is incorrect'
    with allure.step('Проверка что ответ вернул более 1 объекта'):
        assert (len(response.json()['data'])) > 1, 'Not all objects returned'


@allure.feature('API')
@allure.story('Получение объектов')
@allure.title('GET /object/{objectId} - получение одного объекта')
@allure.issue('https://ru.ruwiki.ru/wiki/Бакинская_офицерская_школа_морской_авиации','SCP-222. Подготовка API ч.2')
@allure.id('T1002')
def test_get_one(new_object):
    with allure.step('Вызов метода по REST'):
        response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_object}').json()
    with allure.step('Получен объект по запрошенному id'):
        assert response['id'] == new_object, 'Object not found'


@allure.feature('API')
@allure.story('Создание объектов')
@allure.title('POST /object - создание объекта')
@pytest.mark.parametrize('name', ['ONE MAN', 'twoMan', '123_man'])
def test_post_object(name):
    with allure.step('Создание тестовых данных'):
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
    with allure.step('Проверка что статус ответа 200'):
        assert response.status_code == 200, 'Status code is incorrect'
    with allure.step('Проверка _name_ созданного объекта'):
        assert response.json()['name'] == name, 'The name is incorrect'


@allure.feature('API')
@allure.story('Изменение объекта')
@allure.title('PUT /object/{objectId} - изменение объекта')
@pytest.mark.critical
def test_put_object(new_object):
    with allure.step('Вызов метода по REST'):
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
    with allure.step('Проверка что статус ответа 200'):
        assert response.status_code == 200, 'Status code is incorrect'
    with allure.step('Проверка успешного изменения объекта'):
        assert response.json()['name'] == 'NewPutman', 'The name is incorrect'


@allure.feature('API')
@allure.story('Изменение объекта')
@allure.title('PATCH /object/{objectId} - изменение части объекта')
def test_patch_object(new_object):
    with allure.step('Вызов метода по REST'):
        body = {"name": "NewPatchman"}
        headers = {'Content-Type': 'application/json'}
        response = requests.patch(
            f'http://objapi.course.qa-practice.com/object/{new_object}',
            json=body,
            headers=headers
        )
    with allure.step('Проверка что статус ответа 200'):
        assert response.status_code == 200, 'Status code is incorrect'
    with allure.step('Проверка успешного изменения объекта'):
        assert response.json()['name'] == 'NewPatchman', 'The name is incorrect'


@allure.feature('API')
@allure.story('Удаление объектов')
@allure.title('DELETE /object/{objectId} - удаление объекта по objectId')
def test_delete_object(new_object):
    with allure.step('Вызов метода по REST'):
        response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_object}')
    with allure.step('Проверка содержания ответа'):
        assert response.text == f'Object with id {new_object} successfully deleted', 'Incorrect body response'
    with allure.step('Проверка что статус ответа 200'):
        assert response.status_code == 200, 'Status code is incorrect'
