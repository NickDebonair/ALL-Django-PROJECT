from django.shortcuts import render
from .models import TaggedItem, Kamisama
# Create your views here.
def index(request):
    contents = TaggedItem.objects.all()
    gods = Kamisama.objects.all()
    context = {'content': contents, 'gods': gods}
    return render(request, 'index.html', context)