from django.db.models.signals import post_save
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import mail_managers
from .models import Post

@receiver(post_save, sender=Post)
def notify_managers_appointment(sender, instance, created, **kwargs):
    #subject = f'{instance.title}'
    if created:
        subject = f'{instance.title}'
    else:
        subject = f'{instance.title} changed'
    mail_managers(
        subject=subject,
        message=instance.text,
    )
    print(f'{instance.title}')

# коннектим наш сигнал к функции обработчику и указываем, к какой именно модели после сохранения привязать функцию
# post_save.connect(notify_managers_appointment, sender=Post)