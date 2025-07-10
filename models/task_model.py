from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Task(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    completed: bool = False

    class Config:
        schema_extra = {
            "example":{
                "title": "Ej diseñar logo cliente",
                "description": "El cliente quiere un tipo especifico de logo",
                "due_date": "2025-07-20T23:59:00",
                "completed": False
            }
        }
