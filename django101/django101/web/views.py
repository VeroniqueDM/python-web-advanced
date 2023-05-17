from pyexpat import model

from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from django101.web.models import Todo


def index(request):
    context ={
        'title': 'Function-based view'
    }
    return render(request, 'index.html', context)


class IndexView(generic.View):
    def get(self, request):
        context = {
            'title': 'Class-based view'
        }
        return render(request, 'index.html', context)


class IndexTemplateView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Class-based with TemplateView'
        }
    # # If this class might need to be inherited, then use this alternatively:
    #
    # context = super().get_context_data(**kwargs)
    # context['title'] = 'Class-based with TemplateView'
    # # add other context as needed
    # return context


class RedirectToIndexView(generic.RedirectView):
    url = reverse_lazy('index class-based')

    # def get_redirect_url(self, *args, **kwargs):
    #     if:
    #         place 1
    #     else:
    #         place 2


class TodosListView(generic.ListView):
    model = Todo
    template_name = 'todos-list.html'
    ordering = ('title','category__name')

    # Creating a filter that comes from the url

    def get_queryset(self):
        queryset = super().get_queryset()
        title_filter = self.request.GET.get('filter', None)
        if title_filter:
            queryset = queryset.filter(title__contains=title_filter)
        return queryset


class TodoDetailsView(generic.DetailView):
    model = Todo
    template_name = 'todo-details.html'

class CreateTodoForm:
    pass

class TodoCreateView(generic.CreateView):
    model = Todo
    template_name = 'todo-create.html'
    success_url = reverse_lazy('todos list')
    fields = '__all__'

    # If you want to create your own form and use it:
    form_class = CreateTodoForm
    # Or if you want to pick from forms depending on conditions:
    def get_form_class(self):
        pass
