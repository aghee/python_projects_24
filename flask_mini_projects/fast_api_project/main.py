from fastapi import FastAPI
from models import ToDo

app=FastAPI()

@app.get('/')
async def root():
    return {'message':'hello world'}
todos=[]
#Get all todos
@app.get('/todos')
async def get_todos():
    return {'todos':todos}
#Get single todo
@app.get('/todos/{todo_id}')
async def get_one_todo(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            return {'todo found is':todo}
    return {'message':'todo missing!'}

#Create a todo
@app.post('/todos')
async def create_todos(todo:ToDo):
    todos.append(todo)
    return {'message':'todo item has been created!'}

#update a todo
@app.put('/todos/{todo_id}')
async def update_todo(todo_id:int,todo_obj:ToDo):
    for todo in todos:
        if todo.id==todo_id:
            todo.id=todo_id
            todo.item=todo_obj.item
            return {'todo':todo}
    return {'message':'no todo to update!'}
#delete a todo
@app.delete('/todos/{todo_id}')
async def delete_todo(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            todos.remove(todo)
            return {'message':'todo item deleted!!!'}
    return {'message':'item already deleted!'}