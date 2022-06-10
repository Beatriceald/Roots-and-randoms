from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .models import EquationValues
from .forms import AddEquationValues

# Create your views here.
def equation_roots(request):
    # a * (x**) + b * x + c = 0 - квадратное уравнение
    # b** - 4 * a * c < 0 - нет решений
    # b** - 4 * a * c = 0 - одно решение
    # b** - 4 * a * c > 0 - два решение {
    # x = (-b +- sqrt(b** - 4*a*c))/(2*a)
    # }
    return render(request, 'equation_roots/index.html')

class EquationRootsCreateView(CreateView):
    form_class = AddEquationValues
    template_name = 'equation_roots/index.html'

class EquationRootsDetailView(DetailView):
    model = EquationValues
    template_name = 'equation_roots/solution.html'
    context_object_name = 'solution'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        values = self.get_object()
        context['D'] = int( values.b**2 - 4 * values.a * values.c )
       # context['']  
       # context['']
        return context