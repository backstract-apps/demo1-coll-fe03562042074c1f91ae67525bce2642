from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class User(BaseModel):
    id: int
    Address: str
    first_name: int
    last_name: int
    age: int
    Email Id: str


class ReadUser(BaseModel):
    id: int
    Address: str
    first_name: int
    last_name: int
    age: int
    Email Id: str
    class Config:
        from_attributes = True


