from typing import Union
from pydantic import BaseModel, Field

from fast_api_intro_project.schemas.image import ImageModel


class ItemModel(BaseModel):
    name: str

    # Use Fields to add extra validation and metdata to model attributes
    # set() auto converts a tags list to a unique set for incoming and outgoing data
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None
    tags: set[str] = set()
    images: Union[list[ImageModel], None] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }

