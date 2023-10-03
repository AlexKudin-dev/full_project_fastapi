from typing import Optional
from pydantic import BaseModel, ConfigDict



class UserSchema(BaseModel):
    id: int
    username: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
