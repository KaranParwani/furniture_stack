from typing import Optional
from pydantic import BaseModel


class Furniture(BaseModel):
    '''Schema for Furniture Model'''
    
    name: str
    description: str
    price: float
    comment: Optional[str]
