from db.connection import task_collection
from bson import ObjectId
from schemas.task_schema import task_helper


async def get_tasks():
    tasks = []
    async for task in task_collection.find():
        task.append(task_helper(task))
    return tasks

async def get_task(id: str):
    task = await task_collection.find_one({"_id": ObjectId(id)})
    return task_helper(task) if task else None

async def create_task(task_data: dict):
    task = await task_collection.insert_one(task_data)
    new_task = await task_collection.find_one({"_id": task.inserted_id})
    return task_helper(new_task)

async def update_task(id: str, task_data: dict):
    update_result = await task_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": task_data}
    )
    if update_result.modified_count == 1:
        updated_task = await task_collection.find_one({"_id": ObjectId(id)})
        return task_helper(updated_task)
    return None

async def delete_task(id: str):
    result = await task_collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count == 1