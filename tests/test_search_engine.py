import json
import logging
from api import app


def test_search_by_keyword():
    response = app.test_client().get('/api/v1/songs?keyword=品冠')
    data = json.loads(response.data.decode('utf-8'))
    logging.info(data)
    assert type(data[0]) is dict
    assert type(data[1]) is dict
    assert data[0]['singer'] == '品冠'
    assert data[1]['singer'] == '品冠'
    assert response.status_code == 200
    assert type(data) is list


def test_search_by_keyword():
    response = app.test_client().get('/api/v1/songs?keyword=品冠')
    data = json.loads(response.data.decode('utf-8'))
    logging.info(data)
    assert type(data[0]) is dict
    assert type(data[1]) is dict
    assert data[0]['singer'] == '品冠'
    assert data[1]['singer'] == '品冠'
    assert response.status_code == 200
    assert type(data) is list

