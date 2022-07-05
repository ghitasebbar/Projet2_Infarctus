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
        "score": [0],
        "proba": [[0.9506566135599538,0.04934338644004618]],
        "log_proba": [[-0.05060236096865629,-3.0089515354561653]]
        }

def test_get_score_rf():
    response = client.post(
                "predict/v2",
                headers={"project2_access_token": "OTS7KgBNNBYORI7nVjQeJA"},
            json={"gender": "Female", "age": 29, "hypertension": 0, "heart_disease": 0, "ever_married": "No", "work_type": "Private", "residence_type": "Urban", "avg_glucose_level": 9, "bmi": 20, "smoking_status": "never smoked"}
            )
    assert response.status_code == 200
    assert response.json() == {
        "score": [0],
        "proba": [[0.9875789613590977,0.012421038640902224]],
        "log_proba": [[-0.012498824533587692,-4.388363579491643]]
            }

def test_get_score_bad_token():
    response = client.post(
            "/predict/v1", 
            headers={"project2_access_token": "OTS7KgBNNBYORI7nVgdf"},
            json={"gender": "Female", "age": 29, "hypertension": 0, "heart_disease": 0, "ever_married": "No", "work_type": "Private", "residence_type": "Urban", "avg_glucose_level": 9, "bmi": 20, "smoking_status": "never smoked"}
            )
    assert response.status_code == 403
    assert response.json() == {"detail": "Could not validate X-token header"}

