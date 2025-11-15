from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import SignupForm, TopicForm
from .models import Topic

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()

    return render(request, 'tracker/signup.html', {'form': form})


@login_required
def dashboard_view(request):
    topics = Topic.objects.filter(user=request.user).order_by('-created_at')

    total = topics.count()
    done_count = topics.filter(status='done').count()
    pending_count = total - done_count

    if total > 0:
        progress_percent = int((done_count / total) * 100)
    else:
        progress_percent = 0

    form = TopicForm()

    context = {
        'topics': topics,
        'total': total,
        'done_count': done_count,
        'pending_count': pending_count,
        'progress_percent': progress_percent,
        'form': form,
    }
    return render(request, 'tracker/dashboard.html', context)


@login_required
def add_topic_view(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.save()
    return redirect('dashboard')


@login_required
def toggle_status_view(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)

    if topic.user != request.user:
        return HttpResponseForbidden("You are not allowed to change this topic")

    if topic.status == 'pending':
        topic.status = 'done'
    else:
        topic.status = 'pending'
    topic.save()

    return redirect('dashboard')


@login_required
def delete_topic_view(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)

    if topic.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this topic")

    topic.delete()
    return redirect('dashboard')
