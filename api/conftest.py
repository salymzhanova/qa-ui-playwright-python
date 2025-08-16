import pytest
import os
from api.helpers.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    base_url = os.getenv("API_BASE_URL", "https://reqres.in/api")
    return APIClient(base_url)