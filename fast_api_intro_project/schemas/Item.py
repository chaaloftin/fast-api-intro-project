from typing import Union
from pydantic import BaseModel, Field

from fast_api_intro_project.schemas.image import ImageModel


class ItemModel(BaseModel):
    # Use Fields to add extra validation and metdata to model attributes
    # set() auto converts a tags list to a unique set for incoming and outgoing data
    name: str = Field(examples=["Foo"])
    description: Union[str, None] = Field(default=None, examples=["A very nice Item"])
    price: float = Field(examples=[35.4])
    tax: Union[float, None] = Field(default=None, examples=[3.2])
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
                },
                {
                    "name": "Bar",
                    "price": "35.4",
                },
                {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            ]
        }
    }

