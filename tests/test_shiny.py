"""Tests for the name specific endpoints of the API."""

from litestar import Litestar
from litestar.status_codes import HTTP_200_OK
from litestar.testing import AsyncTestClient


async def test_names(client: AsyncTestClient[Litestar]):
    """Test the /aliases/<name> endpoint.

    Args:
        client (AsyncTestClient[Litestar]): The test client.
    """
    response = await client.get("/alias/shiny")
    assert response.status_code == HTTP_200_OK
    assert "Shiny Quagsire" in response.json()
