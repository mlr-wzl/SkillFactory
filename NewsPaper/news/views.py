from django.views.generic import ListView, DetailView  # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import *
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView, View # импортируем уже знакомый generic
from .filters import *
from django.core.mail import send_mail
from .forms import *  # импортируем нашу форму
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import EmailMultiAlternatives, mail_managers, mail_admins
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views.decorators.csrf import csrf_protect


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

class CommentsList(LoginRequiredMixin,ListView):
    model = Comment  # указываем модель, объекты которой мы будем выводить
    template_name = 'mycomments.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'mycomments'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    paginate_by = 10  # поставим постраничный вывод в один элемент

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        queryset=Comment.objects.filter(post__author__author=user).order_by('-id')
        #return super().get_queryset(*args, **kwargs)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CommentsFilter(self.request.GET, queryset=self.get_queryset())
        return context

class NewsDetailView(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'news_detail.html'  # название шаблона будет onenews.html
    context_object_name = 'onenews'  # название объекта. в нём будет

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'comment_detail.html'  #
    context_object_name = 'onecomment'

class NewsCreateView(PermissionRequiredMixin, CreateView):
    permission_required=('news.add_post')
    template_name = 'news_create.html'
    form_class = NewsForm

    def post(self, request, *args, **kwargs):
        return super(NewsCreateView, self).post(request, **kwargs)

class NewsCommentView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('news.add_post')
    template_name = 'comment_create.html'
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

        post1=request.POST.get('post')
        post2=Post.objects.get(id=post1)
        author1 = Author.objects.get(post=post2.id)
        author2 = Author.objects.get(id=author1.id)
        author3=author2.author
        #comments=Comment.objects.filter(post__author__author=self.request.user).order_by('-id')
        msg = EmailMultiAlternatives(
        subject=f'Новый комментарий к вашему посту "{post2.title}"',
        body=f'Здравствуй {author3.username}. Кто-то добавил новый комментарий!',  # это то же, что и message
        from_email='aleresunova060595@gmail.com',
        to=[f'{author3.email}'],  # это то же, что и recipients_list
        #to=['aleresunova@mail.ru']
        )
        msg.send()  # отсылаем

        return redirect('/')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Comment.objects.get(pk=id)

class NewsUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('news.change_post')
    template_name = 'news_create.html'
    form_class = NewsForm


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class NewsDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'news_delete.html'
    permission_required = ('news.delete_post')
    queryset = Post.objects.all()
    success_url = '/news/'

class CommentDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'comment_delete.html'
    permission_required = ('news.delete_comment')
    queryset = Comment.objects.all()
    success_url = '/news/mycomments'

# class NewsSearchList(ListView):
#     model = Post  # указываем модель, объекты которой мы будем выводить
#     template_name = 'news_search.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
#     context_object_name = 'news_search'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
#     queryset = Post.objects.order_by('-id')
#     paginate_by = 1  # поставим постраничный вывод в один элемент
#
#     def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
#         context = super().get_context_data(**kwargs)
#         context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
#         return context


# class Subscribe(LoginRequiredMixin, View):
#     model = Category
#     def post(self, request, *args, **kwargs):
#         user = self.request.user
#         print(user)
#         category = get_object_or_404(Category, id=self.kwargs['pk'])
#         print(category)
#         if category.subscribers.filter(username=self.request.user).exists():
#             category.subscribers.remove(user)
#         else:
#             category.subscribers.add(user)
#             print(category.subscribers)
#
#         return redirect('/')


class Accept(LoginRequiredMixin, View):
    model = Comment
    def post(self, request, *args, **kwargs):
        user = self.request.user
        onecomment = get_object_or_404(Comment, id=self.kwargs['pk'])
        if onecomment.accepted:
            pass
        else:
            onecomment.accepted = True
            onecomment.save()
            comment_author = onecomment.user
            msg = EmailMultiAlternatives(
                subject=f'Ваш комментарий к посту "{onecomment.post.title}" принят!',
                body=f'Здравствуй {comment_author.username}. Ваш комментарий принят!',  # это то же, что и message
                from_email='aleresunova060595@gmail.com',
                to=[f'{comment_author.email}'],  # это то же, что и recipients_list
                #to=['aleresunova@mail.ru']
            )
            msg.send()  # отсылаем

        return redirect('/news/mycomments')

class CommentFilterView(LoginRequiredMixin, ListView):
    model = Comment  # указываем модель, объекты которой мы будем выводить
    template_name = 'comment_filter.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'comment_filter'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    paginate_by = 10  # поставим постраничный вывод в один элемент

    def get_queryset(self, *args, **kwargs):
        onecomment = get_object_or_404(Comment, id=self.kwargs['pk'])
        queryset=Comment.objects.filter(post=onecomment.post)
        return queryset

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = CommentsFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context




