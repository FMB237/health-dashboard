# This is the python file for writing our simple app tests
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app) # This line tells that we are actualing testing the application with name app

def test_root():
    response =client.get("/")
    assert response.status_code == 200 
    assert "Status" in response.json()

# Let check the health route 
def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'healthy'
