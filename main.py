from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "my user id"}

# path parameters should always go after static paths 
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
            