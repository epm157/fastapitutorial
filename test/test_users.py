from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app import schemas
from app.database import get_db, Base
from app.main import app


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}_test'

#"postgresql://postgres:123456@localhost/fastapi"



engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
Base = declarative_base()

# Dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_root():
    res = client.get("/")
    print(res.json().get('message'))
    assert res.json().get('message') == 'Hello World!'
    assert res.status_code == 200


def test_create_user():
    res = client.post('/users/', json={'email': 'a@ale.de', 'password': 'pass'})
    print(res.json())
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == 'a@ale.de'
    assert res.status_code == 201























