from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel


app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Github KWIATS: ",
        "url": "https://github.com/kwiats",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

users = []


class User(BaseModel):
    username: str
    password: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"username": user}


@app.get("/users/{id}")
async def get_id_user(
    id: int = Path(description="The ID of the user to get"),
    q: str = Query(None, max_length=5),
):
    return {"user": users[id], "query": q}
