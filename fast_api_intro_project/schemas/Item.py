from datetime import date, datetime, time
from typing import Union
from uuid import UUID
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
    uuid: Union[UUID, None] = None
    creation_time: Union[datetime, None] = None
    date_displayed = Union[date, None] = None
    time_displayed = Union[time, None] = None
    byte_representation = Union[bytes, None] = None



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

