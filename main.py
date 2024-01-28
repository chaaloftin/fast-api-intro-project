from enum import Enum
from typing import Optional, Union
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
class ValidUserId(str, Enum):
    Jane = "Jane"
    John = "John"



## USERS ENDPOINTS ##

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "my user id"}

# path parameters should always go after static paths 
# ex: /users/Jane
@app.get("/users/{user_id}")
async def read_user(user_id: ValidUserId):
    if user_id is ValidUserId.Jane:
        return {"user_id": user_id}
    
    if user_id is ValidUserId.John:
        return {"user_id": user_id}


## FILES ENDPOINTS ##

# Dynamic paths can be utilized
# ex: /files/home/johndoe/myfile.txt
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


## ITEMS ENDPOINTS ##

# Query params are function parameters that are not part of the path parameters
# valid Truthy values: on, True, true, 1, yes
# ex: /items?skip=2&limit=3&last_entry_only=anything
@app.get("/items")
async def read_item(skip: int = 0, limit: int = 10, last_entry_only: bool = False):
    items = fake_items_db[skip : skip + limit]

    if (last_entry_only):
        return items[-1]
    return fake_items_db[skip : skip + limit]

# First two params are required
# third param has default value
# fourth param is optional and also accepts None
@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item