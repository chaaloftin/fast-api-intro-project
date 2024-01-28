from typing import Union

from pydantic import BaseModel


class UserModel(BaseModel):
    username: str
    full_name: Union[str, None] = None