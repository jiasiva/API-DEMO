from urllib import request
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
app = FastAPI()

API_KEY= "123456789"
@app.middleware("http")
async def check_api_key (request, call_next):
    key = request.headers.get("X-API-KEY")
    if key != API_KEY:
        return JSONResponse (status_code=401, content={"error": "Unauthorized"})
    return await call_next(request)
@app.get("/")
def home():
    return {"message": "FastAPI server is running successfully!"}
@app.get("/welcome")
def welcome():
    return {"message": "Welcome to my FASTAPI app!"}
@app.get("/user")
def user_profile():
    return {
        "name": "Jeya Lakshmi",
        "channel": "Universe Conquer",
        "Linkedin": "linkedin.com/in/jeyalakshmi05"
    }
@app.get("/user/{user_id}")
def user_profile_by_id(user_id: int):
    if user_id == 1:
        return {
            "user_id": 1,
            "name": "Jeya Lakshmi",
            "role": "AI & IoT Engineer",
            "status": "Active"
        }
    else:
        return {
            "error": "User not found",
            "user_id": user_id
        }
class User(BaseModel):
    name:str
    age:int
    email:str
users=[]

@app.post("/users")
def create_user(user: User):
    users.append(user.model_dump())

    return {"message":"user added successfully","total_users":len(users)}
