import sys
import json
sys.path.append('.')
from app import app


def test_app():
    client = app.test_client()
    headers = {'Content-Type': 'application/json'}
    res = client.post('/api/widgets', data=json.dumps(dict()), headers=headers)
    assert res


def test_app_good():
    client = app.test_client()
    headers = {'Content-Type': 'application/json'}
    res = client.post('/api/widgets', data=json.dumps(dict(name='oop')), headers=headers)
    print res.data
