from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Basic Routes
@app.get("/")
def home():
    return {"message": "Welcome FastAPI"}

@app.get("/about")
def about():
    return {"About": "This website is about E-commerce"}

@app.get("/contact")
def contact():
    return {"Contact": "You can contact us on LinkedIn"}

@app.get("/products")
def products():
    return {"Products": "These are our products"}

# Path Parameter
@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    return {"user_id": user_id}

# Query Parameter
@app.get("/users")
def get_user(name: str = None):
    return {"name": name}

# Multiple Query Parameters
@app.get("/items")
def get_items(name: str = None, price: int = 0):
    return {
        "name": name,
        "price": price
    }

# Create User
@app.get("/create_user")
def create_user(
    name: str,
    age: int,
    college: str,
    semester: int
):
    return {
        "message": "User created",
        "data": {
            "name": name,
            "age": age,
            "college": college,
            "semester": semester
        }
    }