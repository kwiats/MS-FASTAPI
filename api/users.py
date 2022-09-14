from typing import Optional, List
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class User(BaseModel):
    username: str
    password: str
    is_active: bool
    bio: Optional[str]


users = []


@router.get("/users", response_model=List[User])
async def get_users():
    return users


@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"username": user}


@router.get("/users/{id}")
async def get_id_user(id: int):
    return {"user": users[id]}
