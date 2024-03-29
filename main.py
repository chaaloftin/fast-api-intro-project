from enum import Enum
from typing import Annotated, Union
from fastapi import Body, Cookie, FastAPI, Path, Query

from fast_api_intro_project.schemas.Item import ItemModel
from fast_api_intro_project.schemas.user import UserModel


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

# Use Pydantic models from serialization ops and validation
@app.post("/items/")
async def create_item(item: ItemModel):
    item_dict = item.model_dump()

    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})

    return {
        "message": "item created",
        "item": item_dict
    }

# Request body, path, and query parameters decalred in same signature
# If the parameter is also declared in the path, it will be used as a path parameter.
# If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter.
# If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body.
# ex: /items/1?q=example_querygit 
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: ItemModel, q: Union[str, None] = None):
#     result = {"item_id": item_id, **item.model_dump()}
#     if q:
#         result.update({"q": q})
#     return result


# Any Pydantic Model that is added as a param is considered a body param
# Individual non-Pydantic models can be added as body param via Annotated (ex: Annotated[Item, Body(embed=True)])
# Optional body params simply required a default value of None
# Multiple params causes each body param to mapped to a key of the same name
@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: Annotated[int, Path(description="The id for a given item", ge=0, le=1000)],
    item: Annotated[ItemModel, Body(
            examples=[
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ],
        ),
    ],
    user: Union[UserModel, None] = None,
    importance: Annotated[int, Body(gt=0)],
    q: Union[str, None] = None,
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results

# Query params are function parameters that are not part of the path parameters
# valid Truthy values: on, True, true, 1, yes
# ex: /items/?skip=2&limit=3&last_entry_only=anything
# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10, last_entry_only: bool = False):
#     items = fake_items_db[skip : skip + limit]

#     if (last_entry_only):
#         return items[-1]
#     return fake_items_db[skip : skip + limit]

# First two params are required
# third param has default value
# fourth param is optional and also accepts None
# @app.get("/items/{item_id}")
# async def get_user_item(
#     item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
# ):
#     item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
#     return item

# Use Pydantic models from serialization ops and validation
# Using Annotations perform extra validation on params and enhance documentation
# Note that endpoints can deprecated with Query
@app.get("/items/")
async def get_items(
    q: Annotated[
        Union[str, None],
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
    advertisement_id: Annotated[Union[str, None], Cookie()] = None
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Path parameters work just like query params
# gt: greater than
# ge: greater than or equal
# lt: less than
# le: less than or equal
@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


