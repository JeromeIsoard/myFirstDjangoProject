from django.shortcuts import render
from geeps.templates.geeps.forms import PrintingRequestForm


# Create your views here.

def poster_printing_request(request):
    form = PrintingRequestForm()
    return render(request, 'geeps/poster_printing_form.html', {'form': form})


# todo: create models
# todo: register models in admin.py
# todo: create form.py
# todo:
