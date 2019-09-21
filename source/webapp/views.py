from django.shortcuts import render
from webapp.models import Entry


def index_view(request):
    entries = Entry.objects.filter(status='active').order_by('created_at').reverse()
    return render(request, 'index.html', context={
        'entries': entries
    })

