from pydantic import BaseModel, Field
from typing import Optional, List

# Example schemas to guide development

class User(BaseModel):
    username: str
    email: str
    hashed_password: str
    bio: Optional[str] = None

class Product(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    tags: List[str] = []

class Post(BaseModel):
    title: str
    content: str
    author_id: str

class Task(BaseModel):
    title: str
    completed: bool = False
