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

# The todo: dict comes as part of the body- now we don't have a front end, so it'll come form the swagger ui
@api.post('/todos')
def create_todo(todo: dict):
    new_todo_id = max(todo["todo_id"] for todo in all_todos) + 1
    new_todo = {
        "todo_id":new_todo_id,
        "todo_name": todo['todo_name'],
        "todo_description": todo['todo_description']
    }
    all_todos.append(new_todo)

    return new_todo

# The updated_todo will come as part of the body - need to do this through logger
@api.put('/todos/{todo-id}')
def update_todo(todo_id: int, updated_todo: dict):
    for i in all_todos:
        if i['todo_id'] == todo_id:
            i['todo_name'] = updated_todo['todo_name']
            i['todo_description'] = updated_todo['todo_description']
            return i
    return "Error, not found"

# Need to do through logger because we need to provide the delete method
@api.delete('/todos/{todo-id}')
def delete_todo(todo_id: int):
    for h, i in enumerate(all_todos):
        if todo_id == i['todo_id']:
            return all_todos.pop(h)

    return "Error, not found"