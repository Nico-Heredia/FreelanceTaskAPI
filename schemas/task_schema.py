def task_helper(task) -> dict:
    return{
        "id": str (task["_id"]),
        "title": task["title"],
        "description": task.get("description"),
        "due_date": str(task.get("due_date")) if task.get("due_date") else None,
        "completed": task ["completed"]
    }