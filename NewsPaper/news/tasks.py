from celery import shared_task
import datetime
from news.models import Category, Post
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

@shared_task
def mail_to_subs(username, email, title, html_content):
            msg = EmailMultiAlternatives(
                subject=f'{str(title)}',
                body=f'Здравствуй {username}. Новая статья в твоём любимом разделе!',
                from_email='aleresunova060595@gmail.com',
                to=[f'{email}'],
                #to=['aleresunova@mail.ru']
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()

@shared_task
def send_mail_monday():
    end_date = datetime.datetime.now().date()
    start_date = end_date - datetime.timedelta(days=7)
    users = User.objects.all()
    categories = Category.objects.all()
    for one_category in categories:
        subscribers = one_category.subscribers.all()
        if subscribers.exists():
            for subscriber in subscribers:
                list_of_posts = Post.objects.filter(time__range=(start_date, end_date), category=one_category)
                print(list_of_posts)
                html_content = render_to_string(
                    'subs_email_each_month.html',
                    {
                        'news': list_of_posts,
                        'usr': subscriber,
                    }
                )
                msg = EmailMultiAlternatives(
                    subject='New posts of the week',
                    body=f'Здравствуй {subscriber.username}. Новые статьи в твоём любимом разделе!',
                    from_email='aleresunova060595@gmail.com',
                    to=[f'{subscriber.email}'],
                    #to=['aleresunova@mail.ru']
                )
                msg.attach_alternative(html_content, "text/html")  # добавляем html
                msg.send()  # отсылаем









# @shared_task
# def mail_test():
#             msg = EmailMultiAlternatives(
#                 subject='test',
#                 body='test',
#                 # это то же, что и message
#                 from_email='aleresunova060595@gmail.com',
#                 #to=[f'{subscriber.email}'],  # это то же, что и recipients_list
#                 to=['aleresunova@mail.ru']
#             )
#
#             msg.send()  # отсылаем