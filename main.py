from enum import Enum
from fastapi import FastAPI

app = FastAPI()

class ValidUserId(str, Enum):
    Jane = "Jane"
    John = "John"

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "my user id"}

# path parameters should always go after static paths 
@app.get("/users/{user_id}")
async def read_user(user_id: ValidUserId):
    if user_id is ValidUserId.Jane:
        return {"user_id": user_id}
    
    if user_id is ValidUserId.John:
        return {"user_id": user_id}

# Can be used to generate a static path like /files/home/johndoe/myfile.txt
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}