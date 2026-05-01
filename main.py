from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class TodoItem(BaseModel):
    id: int
    title: str
    completed: bool

class TodoList(BaseModel):
    todos: List[TodoItem]

# Todo list ma'lumotlarini saqlash uchun ro'yxat
todos = [
    TodoItem(id=1, title="Buy milk", completed=False),
    TodoItem(id=2, title="Walk the dog", completed=False),
    TodoItem(id=3, title="Do laundry", completed=False)
]

# Todo listni o'qish uchun funksiya
@app.get("/todos", response_model=TodoList)
async def read_todos():
    return TodoList(todos=todos)

# Todo elementini yaratish uchun funksiya
@app.post("/todos", response_model=TodoItem)
async def create_todo(todo: TodoItem):
    todos.append(todo)
    return todo

# Todo elementini o'chirish uchun funksiya
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return {"message": f"Todo with id {todo_id} deleted"}
```

Kodni ishga tushirish uchun FastAPI serverni boshlash uchun quyidagilar qilishingiz kerak:

```bash
uvicorn main:app --reload
```

Bu kodda FastAPI bilan ishlaydigan todo list backend yaratildi. U yaratilgan todo elementlarini o'qish, yaratish va o'chirish uchun funksiyalar mavjud.
