'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'TestSecret'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NzA2MjYxNzIsIm5iZiI6MTY2OTQxNjU3MiwiZW1haWwiOiI8RU1BSUw-In0.Ay3dMuSX7MtISGLtLel_z_ou35sNbwsRR1o2eUug2js'
EMAIL = 'tobititus01@gmail.com'
PASSWORD = 'huff-puff'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'I might run out of text messages to send you, and I might run out of jokes too. My phone might run out of battery, but my heart will never run out of space for you.'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
