from server import api
from fastapi.testclient import TestClient
import json

client = TestClient(api)

def test_get_score_lr():
    response = client.post(
            "/predict/v1",
            headers={"project2_access_token": "OTS7KgBNNBYORI7nVjQeJA"},
            json={"gender": "Female", "age": 29, "hypertension": 0, "heart_disease": 0, "ever_married": "No", "work_type": "Private", "residence_type": "Urban", "avg_glucose_level": 9, "bmi": 20, "smoking_status": "never smoked"}
            )
    assert response.status_code == 200
    assert response.json() == {
        "score": 0 
        }

def test_get_score_lr_bad_token():
    response = client.post(
            "/predict/v1", 
            headers={"project2_access_token": "OTS7KgBNNBYORI7nVgdf"},
            json={"gender": "Female", "age": 29, "hypertension": 0, "heart_disease": 0, "ever_married": "No", "work_type": "Private", "residence_type": "Urban", "avg_glucose_level": 9, "bmi": 20, "smoking_status": "never smoked"}
            )
    assert response.status_code == 403
    assert response.json() == {"detail": "Could not validate X-token header"}

