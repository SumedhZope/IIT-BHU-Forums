from django.shortcuts import render
from .models import group

# Create your views here.
def submit_form(request):
    print (request.POST)
    name = request.POST.get("groupName")
    description = request.POST.get("Description")
    if name is not None and description is not None:
        r = group(name=name,description=description)
        r.save()
    return render( request, "create_groups.html") 
    