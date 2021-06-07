from django.views.generic import ListView, DetailView  # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import *
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView # импортируем уже знакомый generic
from .filters import NewsFilter
from .forms import NewsForm  # импортируем нашу форму
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


# Create your views here.
class NewsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-id')
    paginate_by = 10  # поставим постраничный вывод в один элемент

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context

# class NewsDetail(DetailView):
#     model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
#     template_name = 'onenews.html'  # название шаблона будет onenews.html
#     context_object_name = 'onenews'  # название объекта. в нём будет

class NewsDetailView(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'news_detail.html'  # название шаблона будет onenews.html
    context_object_name = 'onenews'  # название объекта. в нём будет

class NewsCreateView(PermissionRequiredMixin, CreateView):
    permission_required=('news.add_post')
    template_name = 'news_create.html'
    form_class = NewsForm

class NewsUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('news.change_post')
    template_name = 'news_create.html'
    form_class = NewsForm

# метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class NewsDeleteView(DeleteView):
    template_name = 'news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'

class NewsSearchList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'news_search.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news_search'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-id')
    paginate_by = 1  # поставим постраничный вывод в один элемент

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context