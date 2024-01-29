from pydantic import BaseModel, HttpUrl


class ImageModel(BaseModel):
    url: HttpUrl
    name: str