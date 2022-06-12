from random import randint
from django.views.generic import CreateView, DetailView
from .models import Ball
from .forms import AddBallNumber

"""
Функция рандомайзера
"""
def randoms(ball):
    random = []
    blue = 0
    green = 0
    red = 0
    for i in range(0, 100):
        while blue < 50 or green < 30 or red <20:
            random.append(randint(1,3))
            if random[i] == 1:
                blue += 1
                if blue >= 50:
                    break            
            elif random[i] == 2:
                green += 1
                if green >= 30:
                    break
            elif random[i] == 3:
                red += 1
                if red >= 20:
                    break
    return(random[ball])

"""
Класс представления ввода пользовательских данных
"""
class BallNumberCreateView(CreateView):
    form_class = AddBallNumber
    template_name = 'randoms/entry.html'
# Create your views here.

"""
Класс представления вывода цвета предмета
"""
class BallNumberDetailView(DetailView):
    model = Ball
    template_name = 'randoms/output.html'
    context_object_name = 'guess'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        ball = self.get_object()
        context['number'] = ball.ball
        context['randoms'] = randoms(ball.ball)
        context['blue'] = 'Синий цвет'
        context['green'] = 'Зеленый цвет'
        context['red'] = 'Красный цвет'
        return context