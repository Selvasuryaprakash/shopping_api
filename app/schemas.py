from pydantic import BaseModel
from typing import List, Optional


class Login(BaseModel):
    email: str
    password: str

class Signup(BaseModel):
    email: str
    password: str
    con_pass: str
    name: str

# ---------- User ----------
class UserBase(BaseModel):
    name: str
    email: str
    password: str
    phone: str



class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: str
    class Config:
        from_attributes = True

# ---------- Post ----------
class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    user_id: int

class PostOut(PostBase):
    id: str
    user_id: int
    class Config:
        from_attributes = True

# ---------- Comment ----------
class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    user_id: int
    post_id: int

class CommentOut(CommentBase):
    id: str
    user_id: int
    post_id: int
    class Config:
        from_attributes = True
