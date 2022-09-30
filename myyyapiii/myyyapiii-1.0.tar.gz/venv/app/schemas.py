import uuid
from typing import Optional, TypeVar
from fastapi_users import schemas

ID = TypeVar("ID")

class UserRead(schemas.BaseUser[uuid.UUID]):
    org_id: Optional[uuid.UUID] = None
    org_name:str

class UserCreate(schemas.BaseUserCreate):
    org_name: str


class UserUpdate(schemas.BaseUserUpdate):
    pass
