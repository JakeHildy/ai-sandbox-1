import pytest
from httpx import AsyncClient
import app  # Adjust the import path based on your project structure

@pytest.mark.asyncio
async def test_homepage():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.text == "Hello, world!"

@pytest.mark.asyncio
async def test_user_info():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/user")
    assert response.status_code == 200
    assert response.json() == {"name": "John Doe", "age": 30}