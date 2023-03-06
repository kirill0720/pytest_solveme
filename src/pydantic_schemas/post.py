from pydantic import BaseModel, Field


class Post(BaseModel):
    id: int = Field(ge=0)
    title: str
# {'id': 1, 'title': 'POST'}
