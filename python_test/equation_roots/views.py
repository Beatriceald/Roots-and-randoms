import math
from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .models import EquationValues
from .forms import AddEquationValues

"""
Функция нахождения корней
"""
def roots(a, b, c):
    D = b**2 - 4 * a * c
    print("D = ", D)

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif D == 0:
        x = -b / (2 * a)
        return("x = %.2f" % x)
    else:
        return("Нет решений уравнения")

"""
Класс представления ввода пользовательских данных
"""
class EquationRootsCreateView(CreateView):
    form_class = AddEquationValues
    template_name = 'equation_roots/roots.html'

"""
Класс представления вывода решения уравнения
"""
class EquationRootsDetailView(DetailView):
    model = EquationValues
    template_name = 'equation_roots/solution.html'
    context_object_name = 'solution'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        values = self.get_object()
        context['D'] = int( values.b**2 - 4 * values.a * values.c )
        context['roots'] = roots(values.a, values.b, values.c)
        context['no_solution'] = 'Нет решений уравнения'
        context['single_solution'] = 'Одно решение уравнения'
        context['two_solutions'] = 'Два решения уравнения'
        return context