"""Releaseer backend application."""

from typing import Dict, List
from litestar import Litestar, get, post
from releaseer.data import ALIASES
from pydantic import BaseModel


class Alias(BaseModel):
    """Pydantic model for an alias.

    Args:
        BaseModel (Object): The base model.
    """

    name: str
    aliases: List[str]


@get("/")
async def hello() -> Dict[str, str]:
    """Hello from releaseer!

    Returns:
        Dict[str, str]: A simple message.
    """
    return {"message": "Hello from releaseer!"}


@get("/aliases")
async def get_aliases() -> Dict[str, List[str]]:
    """Get all aliases.

    Returns:
        Dict[str, List[str]]: A dictionary of aliases.
    """
    return ALIASES


@post("/alias")
async def post_alias(data: Alias) -> bool:
    """Add an alias to the list of aliases.

    Args:
        data (Alias): The alias to add.
            Alias.name (str): The name of the alias.
            Alias.aliases (List[str]): The list of aliases

    Returns:
        bool: True if the alias was added.
    """
    if not data.name in ALIASES:
        ALIASES[data.name] = []
    ALIASES[data.name].extend(data.aliases)
    return True


@get("/alias/{name:str}")
async def get_alias(name: str) -> List[str]:
    """Get the aliases for a given name.

    Args:
        name (str): The name to get aliases for.

    Returns:
        List[str]: The list of aliases for the given name.
    """
    return ALIASES.get(name, [])


@get("/healthy")
async def healthy() -> bool:
    """Check if the application is healthy.

    Returns:
        bool: True if the application is healthy.
            We are always healthy. :D
    """
    return True


# Create the backend application
app: Litestar = Litestar(
    route_handlers=[hello, get_aliases, post_alias, get_alias, healthy]
)
