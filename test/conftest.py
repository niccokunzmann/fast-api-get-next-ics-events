import os
import sys
import pytest
from fastapi.testclient import TestClient

# relative imports
HERE = os.path.dirname(__file__) or "."
sys.path.append(os.path.join(os.path.abspath(HERE), ".."))
from app import app

@pytest.fixture(scope="module")
def client():
    """The fastapi test client.

    See https://fastapi.tiangolo.com/tutorial/testing/
    """
    return TestClient(app)
