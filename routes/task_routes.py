from fastapi import APIRouter, HTTPException
from controllers.task_controller import (
    get_task, get_tasks, create_task, update_task, delete_task
)
from models.task_model import Task 
from typing import List

router = APIRouter()

@router.get("/tasks", response_model=List[Task])
async def read_tasks():
    return await get_tasks()

@router.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: str):
    task = await get_task(task_id)
    if not task:
        raise HTTPException (status_code=404, detail="Tarea no encontrada")
    return Task

@router.post("/tasks", response_model=Task)
async def create_new_task(task: Task):
    return await create_task(task.dict())

@router.put("/tasks/{task_id}", response_model=Task)
async def update_existing_task(task_id: str, task: Task):
    updated = await update_task(task_id, task.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="No se pudo actualizar")
    return updated

@router.delete("/tasks/{task_id}")
async def delete_existing_task(task_id: str):
    deleted = await delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="No se pudo eliminar")
    raise{"message": "Tarea Eliminada"}