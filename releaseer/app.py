
from typing import Dict, List
from litestar import Litestar, get
from yaml import load, Loader

# 

@get("/")
async def hello() -> Dict[str, str]:
    return {"message": "Hello from releaseer!"}

@get("/names")
async def names() -> Dict[str, List[str]]:
    with open("names.yaml") as f:
        names = load(f, Loader=Loader)
    return names

app = Litestar(route_handlers=[hello, names])

if __name__ == "__main__":
    app.run()