from django.views.generic import ListView, DetailView  # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import *
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView, View # импортируем уже знакомый generic
from .filters import NewsFilter
from django.core.mail import send_mail
from .forms import NewsForm  # импортируем нашу форму
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import EmailMultiAlternatives, mail_managers, mail_admins
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import mail_to_subs

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

class NewsDetailView(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'news_detail.html'  # название шаблона будет onenews.html
    context_object_name = 'onenews'  # название объекта. в нём будет

class NewsCreateView(PermissionRequiredMixin, CreateView):
    permission_required=('news.add_post')
    template_name = 'news_create.html'
    form_class = NewsForm

    def post(self, request, *args, **kwargs):

        html_content = render_to_string(
                'update_created.html',
                {
                    'title': request.POST.get('title'),
                    'text': request.POST.get('text'),
                    'post': Post.objects.all().last().id+1,
                }
            )
        category_2=request.POST.get('category')
        category_3 = Category.objects.get(id=category_2)
        subscribers=category_3.subscribers.all()
        title=request.POST.get('title')
        if subscribers.exists():
            for subscriber in subscribers:
                mail_to_subs.delay(subscriber.username, subscriber.email, title, html_content)
        # commented out for mails without celery
        # if subscribers.exists():
        #     for subscriber in subscribers:
        #         print(subscriber.username)
        #         msg = EmailMultiAlternatives(
        #         subject=f'{str(title)}',
        #         body=f'Здравствуй {subscriber.username}. Новая статья в твоём любимом разделе!',  # это то же, что и message
        #         from_email='aleresunova060595@gmail.com',
        #         to=[f'{subscriber.email}'],  # это то же, что и recipients_list
        #         #to=['aleresunova@mail.ru']
        #         )
        #         msg.attach_alternative(html_content, "text/html")  # добавляем html
        #
        #         msg.send()  # отсылаем
        return super(NewsCreateView, self).post(request, **kwargs)


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


class Subscribe(LoginRequiredMixin, View):
    model = Category
    def post(self, request, *args, **kwargs):
        user = self.request.user
        print(user)
        category = get_object_or_404(Category, id=self.kwargs['pk'])
        print(category)
        if category.subscribers.filter(username=self.request.user).exists():
            category.subscribers.remove(user)
        else:
            category.subscribers.add(user)
            print(category.subscribers)

        return redirect('/')



