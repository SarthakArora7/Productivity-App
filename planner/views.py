from django.shortcuts import render, redirect
from django.views import View
from .models import Task
from .forms import TaskForm
from datetime import date
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

class AddTask(View):
    def get(self, request):
        form = TaskForm()
        return render(request, "planner/add_task.html", {
            "form": form
        })

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.user = request.user
            task.save()
            return redirect("view_tasks")

@method_decorator(login_required, name='dispatch')
class ViewTask(View):
    def get(self, request):
        today = date.today()
        tasks = Task.objects.filter(user=request.user, date=today).order_by('start_time')
        return render(request, 'planner/view_tasks.html', {'tasks': tasks, 'today': today})