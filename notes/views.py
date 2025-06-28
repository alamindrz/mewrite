from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



@login_required
def note_list(request):
    notes = Note.objects.filter(owner=request.user)
    return render(request, 'notes/note_list.html', {'notes': notes})

@login_required
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk, owner=request.user)
    return render(request, 'notes/note_detail.html', {'note': note})

@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

@login_required
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk, owner=request.user)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('note_detail', pk=note.pk)
    return render(request, 'notes/note_form.html', {'form': form})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, owner=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})
    
    
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('note_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})