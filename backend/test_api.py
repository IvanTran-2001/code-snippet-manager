import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestAuth:
    def test_register_success(self):
        response = client.post(
            "/api/auth/register",
            json={"username": "testuser", "email": "test@example.com", "password": "password123"},
        )
        assert response.status_code == 200
        assert response.json()["username"] == "testuser"

    def test_register_duplicate_username(self):
        client.post(
            "/api/auth/register",
            json={"username": "duplicate", "email": "test1@example.com", "password": "pass"},
        )
        response = client.post(
            "/api/auth/register",
            json={"username": "duplicate", "email": "test2@example.com", "password": "pass"},
        )
        assert response.status_code == 400

    def test_login_success(self):
        client.post(
            "/api/auth/register",
            json={"username": "logintest", "email": "login@example.com", "password": "password123"},
        )
        response = client.post(
            "/api/auth/login",
            json={"username": "logintest", "password": "password123"},
        )
        assert response.status_code == 200
        assert "access_token" in response.json()

    def test_login_invalid_password(self):
        client.post(
            "/api/auth/register",
            json={"username": "user123", "email": "user@example.com", "password": "password123"},
        )
        response = client.post(
            "/api/auth/login",
            json={"username": "user123", "password": "wrongpassword"},
        )
        assert response.status_code == 401


class TestSnippets:
    @pytest.fixture
    def auth_token(self):
        client.post(
            "/api/auth/register",
            json={"username": "snippetuser", "email": "snippet@example.com", "password": "pass"},
        )
        response = client.post(
            "/api/auth/login",
            json={"username": "snippetuser", "password": "pass"},
        )
        return response.json()["access_token"]

    def test_create_snippet(self, auth_token):
        headers = {"Authorization": f"Bearer {auth_token}"}
        response = client.post(
            "/api/snippets",
            json={
                "title": "Python Loop",
                "code": "for i in range(10): print(i)",
                "language": "python",
            },
            headers=headers,
        )
        assert response.status_code == 200
        assert response.json()["title"] == "Python Loop"

    def test_list_snippets(self, auth_token):
        headers = {"Authorization": f"Bearer {auth_token}"}
        client.post(
            "/api/snippets",
            json={
                "title": "Test Snippet",
                "code": "print('hello')",
                "language": "python",
            },
            headers=headers,
        )
        response = client.get("/api/snippets", headers=headers)
        assert response.status_code == 200
        assert len(response.json()) > 0
