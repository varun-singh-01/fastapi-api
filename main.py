# Import FastAPI and Utilities
from fastapi import FastAPI
from typing import Optional

# Create FastAPI app
app = FastAPI()

# Synchronous API To Return a Json Response
@app.get("/hello")
def read_root():
    return {"Hello": "FastAPI"}
