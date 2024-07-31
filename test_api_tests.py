import requests

# Найти книгу по названию

def test_api():
    base_URL = 'https://web-gate.chitai-gorod.ru/api/v1'
    headers = {
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjIwNDg0MDEsImlhdCI6MTcyMTg4MDQwMSwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6Ijg3NTMxNzBjNjczZjk3MDBmMjRhMzM1ZjFkYmIwMThlOWYzMGZhMzQ3MDIxZjEwMDk4MWVjOGYxMTA5OGI5ZmUiLCJ0eXBlIjoxMH0.Kb2xUmmk1gEFUcWAW9QYHamqwun28w3OVQGErZFNamc'
    }
    response = requests.get(base_URL + '/recommend/semantic?phrase=Мастер и Маргарита&perPage=48', headers=headers)
    assert response.status_code == 200

# Найти книгу по ID

def test_api():
    base_URL = 'https://web-gate.chitai-gorod.ru/api/v1'
    headers = {
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjIwNDg0MDEsImlhdCI6MTcyMTg4MDQwMSwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6Ijg3NTMxNzBjNjczZjk3MDBmMjRhMzM1ZjFkYmIwMThlOWYzMGZhMzQ3MDIxZjEwMDk4MWVjOGYxMTA5OGI5ZmUiLCJ0eXBlIjoxMH0.Kb2xUmmk1gEFUcWAW9QYHamqwun28w3OVQGErZFNamc'
    }
    response = requests.get(base_URL + '/products/slug/master-i-margarita-3018590', headers=headers)
    assert response.status_code == 200

# Получить список магазинов

def test_api():
    base_URL = 'https://web-gate.chitai-gorod.ru/api/v1'
    headers = {
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjIwNDg0MDEsImlhdCI6MTcyMTg4MDQwMSwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6Ijg3NTMxNzBjNjczZjk3MDBmMjRhMzM1ZjFkYmIwMThlOWYzMGZhMzQ3MDIxZjEwMDk4MWVjOGYxMTA5OGI5ZmUiLCJ0eXBlIjoxMH0.Kb2xUmmk1gEFUcWAW9QYHamqwun28w3OVQGErZFNamc'
    }
    response = requests.get(base_URL + '/shops-cities', headers=headers)
    assert response.status_code == 200 

# Получить список категорий

def test_api():
    base_URL = 'https://web-gate.chitai-gorod.ru/api/v2'
    headers = {
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjIwNDg0MDEsImlhdCI6MTcyMTg4MDQwMSwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6Ijg3NTMxNzBjNjczZjk3MDBmMjRhMzM1ZjFkYmIwMThlOWYzMGZhMzQ3MDIxZjEwMDk4MWVjOGYxMTA5OGI5ZmUiLCJ0eXBlIjoxMH0.Kb2xUmmk1gEFUcWAW9QYHamqwun28w3OVQGErZFNamc'
    }
    response = requests.get(base_URL + '/categories', headers=headers)
    assert response.status_code == 200

# Поиск книги в определенной стране

def test_api():
    base_URL = 'https://web-gate.chitai-gorod.ru/api/v1'
    headers = {
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjIwNDg0MDEsImlhdCI6MTcyMTg4MDQwMSwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6Ijg3NTMxNzBjNjczZjk3MDBmMjRhMzM1ZjFkYmIwMThlOWYzMGZhMzQ3MDIxZjEwMDk4MWVjOGYxMTA5OGI5ZmUiLCJ0eXBlIjoxMH0.Kb2xUmmk1gEFUcWAW9QYHamqwun28w3OVQGErZFNamc'
    }
    response = requests.get(base_URL + '/countries', headers=headers)
    assert response.status_code == 200
