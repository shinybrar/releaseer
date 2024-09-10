from litestar import Litestar
from litestar.status_codes import HTTP_200_OK
from litestar.testing import AsyncTestClient

async def test_healthy(client: AsyncTestClient[Litestar]):
    response = await client.get("/healthy")
    assert response.status_code == HTTP_200_OK
    assert response.json() is True

async def test_hello(client: AsyncTestClient[Litestar]):
    response = await client.get("/")
    assert response.status_code == HTTP_200_OK
    assert response.json() == {"message": "Hello from releaseer!"}

async def test_names(client: AsyncTestClient[Litestar]):
    response = await client.get("/names")
    assert response.status_code == HTTP_200_OK
    assert "names" in response.json()
    assert isinstance(response.json()["names"], list)