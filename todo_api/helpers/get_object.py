from ..models import Todo 

def get_object(todo_id, user_id):
    try:
        return Todo.objects.get(id= todo_id, user= user_id)
    except Todo.DoesNotExist:
        return None
