# Import fastapi class from the module FastAPI
from fastapi import FastAPI

api = FastAPI()

# In memory storage for now- eventually replace with sql database
all_todos = [{"todo_id":1, "todo_name":"sports", "todo_description":"Go to the arena"},
             {"todo_id":2, "todo_name": "eat", "todo_description":"Make pizza"},
             {"todo_id":3, "todo_name":"shop", "todo_description":"Go to costco"},
             {"todo_id":4, "todo_name":"meditate", "todo_description":"meditate"},
             {"todo_id":5, "todo_name":"gym", "todo_description":"Go to the gym"}
]

# GET - to get information, POST - create something, POST - changing something, DELETE- deleting something
# The basic structure of creating an endpont in fastapi is to to @api.{method}('path')

@api.get('/')
def index():
    return {"message":"Hello-word"}

# User passes todo_id via the url as a path parameter- basically this is the path to a specific resource
@api.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return {"result":todo}

# Get all the todos or filter by a query parameter
@api.get('/todos')
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos
