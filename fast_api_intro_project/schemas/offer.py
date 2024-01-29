from typing import Union
from pydantic import BaseModel

from fast_api_intro_project.schemas.Item import ItemModel


class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: list[ItemModel]