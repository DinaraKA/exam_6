from django.shortcuts import render, redirect
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