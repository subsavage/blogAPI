from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import List, Optional

class Blog(BaseModel):
    title: str
    content: str
    hashtags: Optional[List[str]] = []
    photo: Optional[UploadFile] = None