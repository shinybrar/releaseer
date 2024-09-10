from typing import TYPE_CHECKING
from collections.abc import AsyncIterator

import pytest

from litestar.testing import AsyncTestClient

from releaseer.app import app

if TYPE_CHECKING:
    from litestar import Litestar

@pytest.fixture(scope="function")
async def client() -> AsyncIterator[AsyncTestClient[Litestar]]:
    async with AsyncTestClient(app) as client:
        yield client