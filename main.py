from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

blogs = []

class Blog(BaseModel):
    title: str
    content: str
    hashtags: Optional[List[str]] = []
    photo: Optional[UploadFile] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/createablog")
async def create_blog(blog: Blog):
    if blog.photo:
        print(f"Received file: {blog.photo.filename}")
    new_blog = blog.json()
    blogs.append(new_blog)
    
    return new_blog

@app.get("/blogs/")
async def get_blogs():
    return blogs
