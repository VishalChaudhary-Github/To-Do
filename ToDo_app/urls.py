from django.urls import path
from ToDo_app.views import home, add_task, del_task, task_done


urlpatterns = [path('', home, name='todo-home'),
               path('add-task', add_task, name='add-task'),
               path('del-task/<int:task_id>', del_task, name='del-task'),
               path('task-done/<int:task_id>', task_done, name='task-done')
               ]