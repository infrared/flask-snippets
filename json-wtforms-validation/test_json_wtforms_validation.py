import sys
import json
sys.path.append('.')
from app import app


def test_app_bad_validation():
    client = app.test_client()
    headers = {'Content-Type': 'application/json'}
    res = client.post('/api/widgets', data=json.dumps(dict()), headers=headers)
    data = json.loads(res.data)
    assert data.get('name')[0] == "This field is required."


def test_app_bad_validation_name():
    client = app.test_client()
    headers = {'Content-Type': 'application/json'}
    res = client.post('/api/widgets', data=json.dumps(dict(name='bar')),
                      headers=headers)
    data = json.loads(res.data)
    assert data.get('name')[0].startswith('Invalid value')


def test_app_good():
    client = app.test_client()
    headers = {'Content-Type': 'application/json'}
    res = client.post('/api/widgets', data=json.dumps(dict(name='oop')),
                      headers=headers)
    data = json.loads(res.data)
    assert data.get('message') == "Thanks for the widget"


def test_app_good_non_json():
    client = app.test_client()
    res = client.post('/api/widgets', data=dict(name='oop'))
    data = json.loads(res.data)
    assert data.get('message') == "Thanks for the widget"
