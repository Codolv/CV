from django.views import generic
from .models import Person


# Create your views here.
class CVView(generic.DetailView):
    model = Person
    template_name = 'person/cv.html'
