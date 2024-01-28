from typing import Union
from pydantic import BaseModel, Field


class ItemModel(BaseModel):
    name: str

    # Use Fields to 
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None

