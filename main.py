# Import fastapi class from the module FastAPI
from fastapi import FastAPI

api = FastAPI()

# GET - to get information, POST - create something, POST - changing something, DELETE- deleting something

# The basic structure of creating an endpont in fastapi is to to @api.{method}('path')
@api.get('/')
def index():
    return {"message":"Hello-world"}

