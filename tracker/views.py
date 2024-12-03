from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, HabitLog
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from .forms import HabitForm, HabitLogForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

@login_required
def habit_list(request):
    habits = Habit.objects.filter(created_by=request.user)
    context = {"habits": habits}
    return render(request, "tracker/habit_list.html", context)

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit  = form.save(commit=False)
            habit.created_by = request.user
            habit.save()
            messages.success(request, "You have added a new habit")
            return redirect("habit_list")
    else:
        form = HabitForm()
    return render(request, 'tracker/add_habit.html', {'form': form})

@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit.delete()
    messages.success(request, f"You have deleted {habit.name}")
    return redirect("habit_list")

@login_required
def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk, created_by=request.user)
    logs = HabitLog.objects.filter(habit=habit)
    print(logs)
    context = {'habit': habit, "logs": logs}
    return render(request, 'tracker/habit_detail.html', context)

@login_required
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "POST":
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            messages.success(request, "Habit updated successfully")
            return redirect("habit_detail", pk=habit.pk)
    else:
        form = HabitForm(instance=habit)
        context = { 'form': form, 'habit': habit}
    return render(request, 'tracker/edit_habit.html', context)

@login_required
def add_log(request, pk):
    habit = Habit.objects.get(pk=pk)
    if request.method == "POST":
        form = HabitLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.habit = habit
            log.save()
            messages.success(request, "Log added successfully")
            return redirect('habit_detail', pk=habit.pk)
    else:
        form = HabitLogForm()
    context = {'form': form, "habit": habit}
    return render(request, 'tracker/add_log.html', context)

@login_required
def change_habit_log_status(request, pk):
    habit_log = get_object_or_404(HabitLog, pk=pk)

    if habit_log.status:
        HabitLog.objects.filter(pk=pk).update(status=False)
    
    if not habit_log.status:
        habit_log.status = True
        habit_log.save()
    
    return redirect('habit_detail', pk=habit_log.habit.pk)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("habit_list")
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'tracker/register.html', context)