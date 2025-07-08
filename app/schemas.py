from pydantic import BaseModel
from typing import List, Optional

# ---------- User ----------
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int
    class Config:
        orm_mode = True

# ---------- Post ----------
class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    user_id: int

class PostOut(PostBase):
    id: int
    user_id: int
    class Config:
        orm_mode = True

# ---------- Comment ----------
class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    user_id: int
    post_id: int

class CommentOut(CommentBase):
    id: int
    user_id: int
    post_id: int
    class Config:
        orm_mode = True
