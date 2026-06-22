import importlib.util
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient

MODULE_PATH = Path(__file__).resolve().parents[1] / "uberAPI.py"


class DummyModel:
    def predict(self, _):
        return [42.126]


def load_app_module():
    spec = importlib.util.spec_from_file_location("uber_api_test_module", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    with patch("joblib.load", return_value=DummyModel()):
        assert spec is not None
        assert spec.loader is not None
        spec.loader.exec_module(module)
    return module


def test_predict_endpoint_returns_rounded_fare():
    module = load_app_module()
    client = TestClient(module.app)
    response = client.post(
        "/predict",
        json={
            "passenger_count": 1,
            "hour": 12,
            "weekday": 3,
            "month": 8,
            "year": 2024,
            "is_weekday": 1,
            "is_night": 0,
            "distance_km": 5.5,
        },
    )
    assert response.status_code == 200
    assert response.json() == {"predicted_fare": 42.13}


def test_home_endpoint_returns_html():
    module = load_app_module()
    client = TestClient(module.app)
    response = client.get("/")
    assert response.status_code == 200
    assert "<!DOCTYPE html>" in response.text
