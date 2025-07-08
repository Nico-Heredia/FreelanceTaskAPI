from fastapi import FastAPI
from routes.task_routes import router as TaskRouter
from routes.task_routes import router as task_router


app.include_router(task_router)

app = FastAPI(
    title="Freelance Task API",
    description="API para gestionar tareas de proyectos freelance",
    version="1.0.0"

)

#incluimos rutas de tareas
app.include_router(TaskRouter)
