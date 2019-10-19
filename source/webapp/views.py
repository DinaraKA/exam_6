from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Entry
from webapp.form import EntryForm


def index_view(request):
    entries = Entry.objects.filter(status='active').order_by('created_at').reverse()
    return render(request, 'index.html', context={
        'entries': entries
    })

def entry_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = EntryForm()
        return render(request, 'create.html', context={'form': form})
    elif request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            Entry.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text']
            )
            return redirect('index')
        else:
            return render(request, 'create.html', context={'form': form})


def entry_edit(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'GET':
        form = EntryForm(data={
            'name': entry.name,
            'email': entry.email,
            'text': entry.text
        })
        return render(request, 'edit.html', context={'form': form, 'entry': entry})
    elif request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry.name = form.cleaned_data['name']
            entry.email = form.cleaned_data['email']
            entry.text = form.cleaned_data['text']
            entry.save()
            return redirect('index')
        else:
            return render(request, 'edit.html', context={'form': form, 'entry': entry})

def delete_view(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'entry':entry})
    elif request.method == 'POST':
        entry.delete()
        return redirect('index')

