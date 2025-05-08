from fastapi import FastAPI
from pydantic import BaseModel
from ia.api.copilot_api import AssistantIA
from ia.task_manager import TaskManager

app = FastAPI()

class TaskRequest(BaseModel):
    task_description: str

assistant = AssistantIA(api_key="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")
task_manager = TaskManager(api_key="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")

@app.post("/generate-code/")
def generate_code(task_description: str):
    result = assistant.handle_task(task_description)
    return {"task": task_description, "generated_code": result}

@app.post("/add-task/")
def add_task(task: TaskRequest):
    task_manager.add_task(task.task_description)
    return {"message": f"Tâche ajoutée : {task.task_description}"}

@app.post("/automate/")
def automate(task: TaskRequest):
    result = task_manager.automate_development(task.task_description)
    return result