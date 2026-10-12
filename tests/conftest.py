import pytest
from fastapi.testclient import TestClient

from app.database import engine
from app.main import app
from app.models import Base


@pytest.fixture(autouse=True)
def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


@pytest.fixture
def client():
    return TestClient(app)
