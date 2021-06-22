import logging
import datetime

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from news.models import Category, Post
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import EmailMultiAlternatives


logger = logging.getLogger(__name__)


def my_job():
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=7)
    print('выполнение началось')
    for u in User.objects.all():
        if len(u.category_set.all()) > 0:
            list_of_posts = Post.objects.filter(time__range=(start_date, end_date),
                                                category__in=u.category_set.all())
            html_content = render_to_string(
                'subs_email_each_month.html',
                {
                    'news': list_of_posts,
                    'usr': u,
                }
            )

    users = User.objects.all()
    # print(users)
    categories = Category.objects.all()
    # print(category)
    #subscribers = category_3.subscribers.all()
    for category in categories:
        subscribers = category.subscribers.all()
        if subscribers.exists():
            for subscriber in subscribers:
                print(subscriber.username)
                msg = EmailMultiAlternatives(
                subject='New posts of the week',
                body=f'Здравствуй {subscriber.username}. Новые статьи в твоём любимом разделе!',  # это то же, что и message
                from_email='aleresunova060595@gmail.com',
                #to=[f'{subscriber.email}'],  # это то же, что и recipients_list
                to=['aleresunova@mail.ru']
                )
                msg.attach_alternative(html_content, "text/html")  # добавляем html
                msg.send()  # отсылаем





# функция, которая будет удалять неактуальные задачи
def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # добавляем работу нашему задачнику
        scheduler.add_job(
            my_job,
            trigger=CronTrigger(second="*/10"),
            # То же, что и интервал, но задача тригера таким образом более понятна django
            id="my_job",  # уникальный айди
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            # Каждую неделю будут удаляться старые задачи, которые либо не удалось выполнить, либо уже выполнять не надо.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")