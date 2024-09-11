"""Pytest configuration file for the tests."""

from collections.abc import AsyncIterator

import pytest

from litestar.testing import AsyncTestClient

from releaseer.app import app


from litestar import Litestar


@pytest.fixture(scope="function")
async def client() -> AsyncIterator[AsyncTestClient[Litestar]]:
    """Fixture for the async test client.

    Returns:
        AsyncIterator[AsyncTestClient[Litestar]]: An async test client.

    Yields:
        Iterator[AsyncIterator[AsyncTestClient[Litestar]]]: An async test client.
    """
    async with AsyncTestClient(app) as client:
        yield client
