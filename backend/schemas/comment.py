from pydantic import BaseModel


class Comment(BaseModel):
    '''Schema for Comment Model'''
    
    comment: str
