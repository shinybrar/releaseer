"""Tests for the base endpoints of the API."""

from litestar import Litestar
from litestar.status_codes import HTTP_200_OK, HTTP_201_CREATED
from litestar.testing import AsyncTestClient


async def test_healthy(client: AsyncTestClient[Litestar]):
    """Test the /healthy endpoint.

    Args:
        client (AsyncTestClient[Litestar]): The test client.
    """
    response = await client.get("/healthy")
    assert response.status_code == HTTP_200_OK
    assert response.json() is True


async def test_hello(client: AsyncTestClient[Litestar]):
    """Test the / endpoint.

    Args:
        client (AsyncTestClient[Litestar]): The test client.
    """
    response = await client.get("/")
    assert response.status_code == HTTP_200_OK
    assert response.json() == {"message": "Hello from releaseer!"}


async def test_names(client: AsyncTestClient[Litestar]):
    """Test the /aliases endpoint.

    Args:
        client (AsyncTestClient[Litestar]): The test client.
    """
    response = await client.get("/aliases")
    assert response.status_code == HTTP_200_OK
    assert "shiny" in response.json()
    assert "Shiny Quagsire" in response.json()["shiny"]


async def test_add_alias(client: AsyncTestClient[Litestar]):
    """Test adding an alias.

    Args:
        client (AsyncTestClient[Litestar]): The test client.
    """
    response = await client.post(
        "/alias", json={"name": "tester", "aliases": ["Testie McFluff"]}
    )
    assert response.status_code == HTTP_201_CREATED
    assert response.json() is True
    # Check that the alias was added
    response = await client.get("/alias/tester")
    assert response.status_code == HTTP_200_OK
    assert "Testie McFluff" in response.json()
    # Check that the alias was added to the list of all aliases
    response = await client.get("/aliases")
    assert response.status_code == HTTP_200_OK
    assert "tester" in response.json()
    assert "shiny" in response.json()
