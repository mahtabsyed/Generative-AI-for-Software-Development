import pytest
from security_vulerability import app, db, User
from werkzeug.security import generate_password_hash

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_home(client):
    rv = client.get('/')
    assert b"Welcome to the Security Testing Demo!" in rv.data

def test_get_users(client):
    rv = client.get('/users')
    assert rv.status_code == 200
    assert rv.json == []

def test_add_user(client):
    rv = client.post('/user', json={"username": "testuser", "password": "testpassword"})
    assert rv.status_code == 201
    assert b"User added successfully" in rv.data

def test_add_user_missing_fields(client):
    rv = client.post('/user', json={"username": "testuser"})
    assert rv.status_code == 400
    assert b"Username and password are required" in rv.data

def test_add_user_duplicate_username(client):
    client.post('/user', json={"username": "testuser", "password": "testpassword"})
    rv = client.post('/user', json={"username": "testuser", "password": "testpassword"})
    assert rv.status_code == 400
    assert b"Username already exists" in rv.data

def test_get_user(client):
    client.post('/user', json={"username": "testuser", "password": "testpassword"})
    rv = client.get('/user/1')
    assert rv.status_code == 200
    assert rv.json['username'] == "testuser"

def test_get_user_not_found(client):
    rv = client.get('/user/1')
    assert rv.status_code == 404
    assert b"User not found" in rv.data

def test_update_user(client):
    client.post('/user', json={"username": "testuser", "password": "testpassword"})
    rv = client.put('/user/1', json={"username": "updateduser", "password": "updatedpassword"})
    assert rv.status_code == 200
    assert b"User updated successfully" in rv.data

def test_update_user_not_found(client):
    rv = client.put('/user/1', json={"username": "updateduser", "password": "updatedpassword"})
    assert rv.status_code == 404
    assert b"User not found" in rv.data

def test_update_user_missing_fields(client):
    client.post('/user', json={"username": "testuser", "password": "testpassword"})
    rv = client.put('/user/1', json={"username": "updateduser"})
    assert rv.status_code == 400
    assert b"Username and password are required" in rv.data

def test_delete_user(client):
    client.post('/user', json={"username": "testuser", "password": "testpassword"})
    rv = client.delete('/user/1')
    assert rv.status_code == 200
    assert b"User deleted successfully" in rv.data

def test_delete_user_not_found(client):
    rv = client.delete('/user/1')
    assert rv.status_code == 404
    assert b"User not found" in rv.data

def test_sql_injection(client):
    malicious_username = "'; DROP TABLE users; --"
    rv = client.post('/user', json={"username": malicious_username, "password": "testpassword"})
    assert rv.status_code == 400 or rv.status_code == 500

def test_password_hashing(client):
    client.post('/user', json={"username": "testuser", "password": "testpassword"})
    user = User.query.filter_by(username="testuser").first()
    assert user is not None
    assert user.password != "testpassword"
    assert user.password.startswith("pbkdf2:sha256")


if __name__ == "__main__":
    pytest.main()
