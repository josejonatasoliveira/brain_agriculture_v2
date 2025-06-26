from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

def test_create_producer(client: TestClient, db: Session):
    # GIVEN
    response = client.post(
        "/producers/",
        json={
            "cpf_cnpj": "12345678901",
            "name": "John Doe",
            "farm_name": "Green Acres",
            "city": "Ruralville",
            "state": "RS",
            "total_area": 1000.0,
            "agricultural_area": 500.0,
            "vegetation_area": 300.0
        },
    )

    # WHE/THEN
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"
    assert "id" in data

def test_read_producers(client: TestClient, db: Session):
    # GIVEN
    response = client.get("/producers/")

    # WHEN/THEN
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_producer(client: TestClient, db: Session):
    # GIVEN
    producer_data = {
        "cpf_cnpj": "11122233344",
        "name": "Jane Doe",
        "farm_name": "Blue Hills",
        "city": "Farmtown",
        "state": "SC",
        "total_area": 500.0,
        "agricultural_area": 200.0,
        "vegetation_area": 100.0
    }

    # WHEN
    create_response = client.post("/producers/", json=producer_data)
    producer_id = create_response.json()["id"]

    response = client.get(f"/producers/{producer_id}")

    # THEN
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Jane Doe"

def test_update_producer(client: TestClient, db: Session):
    # GIVEN
    producer_data = {
        "cpf_cnpj": "55566677788",
        "name": "Bob Smith",
        "farm_name": "Red Barn",
        "city": "Countryside",
        "state": "PR",
        "total_area": 700.0,
        "agricultural_area": 350.0,
        "vegetation_area": 150.0
    }

    # WHEN
    create_response = client.post("/producers/", json=producer_data)
    producer_id = create_response.json()["id"]

    updated_data = {
        "cpf_cnpj": "55566677788",
        "name": "Robert Smith",
        "farm_name": "Red Barn",
        "city": "Countryside",
        "state": "PR",
        "total_area": 700.0,
        "agricultural_area": 350.0,
        "vegetation_area": 150.0
    }
    response = client.put(f"/producers/{producer_id}", json=updated_data)

    # THEN
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Robert Smith"

def test_delete_producer(client: TestClient, db: Session):
    # GIVEN
    producer_data = {
        "cpf_cnpj": "99988877766",
        "name": "Alice Brown",
        "farm_name": "Yellow Fields",
        "city": "Green Valley",
        "state": "SP",
        "total_area": 200.0,
        "agricultural_area": 100.0,
        "vegetation_area": 50.0
    }

    # WHEN
    create_response = client.post("/producers/", json=producer_data)
    producer_id = create_response.json()["id"]

    response = client.delete(f"/producers/{producer_id}")

    # THEN
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Alice Brown"

    get_response = client.get(f"/producers/{producer_id}")
    assert get_response.status_code == 404


