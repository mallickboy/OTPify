import os
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from pathlib import Path
from typing import Optional
from pydantic import BaseModel

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / '.env')
server_host = os.getenv("SERVER_HOST", "0.0.0.0")
server_port = int(os.getenv("SERVER_PORT", 8080)) # host and port will not work for uvicorn

app= FastAPI() # creating instance of FastAPI

# routes
@app.get("/")       #   @app : path operation decorator   .get : operation on the path /
async def root():   #   path operation function
    return {"message":"hellow world"}


@app.get("/blog") # query parameter /blog?limit=5
async def about(limit: int =10, published: bool= True, sort: Optional[str]= None):
    return {"data":f"getting blog upto : {limit} from db && published : {published}"}

@app.get("/blog/other")
async def about():
    return {"data":"other"}

@app.get("/blog/{id}") # path parameter {id}
async def about(id: int):
    return {"data":id,
            "host":server_host,
            "port":server_port}

@app.get("/blog/{id}/comments")
async def comments(id: int, limit: int= 10): # {id} path parameter and ? limit query parameter 
    return {"data":{1:"hii",2:"goog work"}}



## POST
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/blog")
async def create_blog(req: Item):
    return {"data":"Blog is created", "req":req} 


# if __name__ == "__main__":  # required if running via python 3 directly
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)