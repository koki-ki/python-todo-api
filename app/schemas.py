from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    email: str

class ToDoListSchema(BaseModel):
    id: int
    name: str
    user_id: int

class ToDoSchema(BaseModel):
    id: int
    text: str
    done: bool
    todo_list_id: int
