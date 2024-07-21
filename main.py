from typing import Annotated

from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()

storage: dict[str, str] = {}


class Clip(BaseModel):
    message: str


@app.get("/clip")
async def get_clip(user: Annotated[str | None, Header()] = None):
    clip = storage.get(user, None)

    if clip is not None:
        del storage[user]

    return {"clip": storage.get(user, None)}


@app.post("/clip")
async def save_clip(clip: Clip, user: Annotated[str | None, Header()] = None):
    storage[user] = clip.message
    return {"saved": True, "clip": storage.get(user, None)}
