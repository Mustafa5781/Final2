from django.shortcuts import render, redirect, get_object_or_404
from account.models import Account
from django.contrib.auth.decorators import login_required
from .models import Task


@login_required
def home(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        title = request.POST['task-title']
        description = request.POST['description']
        priority = request.POST['priority']
        due_date = request.POST['due_date']
        is_completed = True if request.POST.get('is_completed') == "YES" else False

        if task_id:  # If task_id exists, update existing task
            task = get_object_or_404(Task, id=task_id, owner=request.user)
            task.title = title
            task.description = description
            task.priority = priority
            task.due_date = due_date
            task.complete = is_completed
            task.save()
        else:  # Create new task
            Task.objects.create(
                title=title,
                owner=request.user,
                description=description,
                priority=priority,
                complete=is_completed,
                due_date=due_date,
            )

    tasks = Task.objects.filter(owner=request.user)
    active_tasks = tasks.filter(complete=False).count()
    completed_tasks = tasks.count() - active_tasks
    context = {
        'tasks': tasks,
        'active_tasks': active_tasks,
        'completed_tasks': completed_tasks,
        'username': request.user.username,
    }
    return render(request, 'home.html', context)


@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, owner=request.user)
    task.delete()
    return redirect('home')
