from pydantic import BaseModel, Field
from typing import Optional

# Define schemas here. Each class name corresponds to a MongoDB collection with the lowercase name.

class Score(BaseModel):
    player: Optional[str] = Field(default="Guest")
    distance: float = 0.0
    timestamp: Optional[str] = None
