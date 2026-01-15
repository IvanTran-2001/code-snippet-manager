from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    pass


class Tag(TagBase):
    id: int

    class Config:
        from_attributes = True


class SnippetBase(BaseModel):
    title: str
    description: Optional[str] = None
    code: str
    language: str
    is_public: bool = False


class SnippetCreate(SnippetBase):
    tags: Optional[List[str]] = []


class SnippetUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    code: Optional[str] = None
    language: Optional[str] = None
    is_public: Optional[bool] = None
    tags: Optional[List[str]] = None


class Snippet(SnippetBase):
    id: int
    user_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    view_count: int
    tags: List[Tag]

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
