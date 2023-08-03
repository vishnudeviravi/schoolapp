from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import Person

# Create your views here.


# def home(request):
#     return render(request, 'schoolapp/home.html')


class Home(View):

    def get(self, request, *args, **kwargs):
        person = Person.objects.get(id=1)
        return render(request, 'schoolapp/home.html', {'person': person})


class About(TemplateView):
    template_name = 'schoolapp/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'apple'
        context['person'] = Person.objects.get(id=1)
        return context


class Blog(ListView):
    model = Person
    template_name = 'schoolapp/blog.html'
    context_object_name = 'persons'


class DetailPage(DetailView):
    model = Person
    template_name = 'schoolapp/detailpage.html'
    context_object_name = 'person'
