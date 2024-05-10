from django.test import TestCase
from .models import Response, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives

@receiver(post_save, sender=Response)
def subscriptions_post_created(instance, created, **kwargs):
    if not created:
        return

    emails = User.objects.filter().values_list('email', flat=True)
        
    subject = f'New post: {instance.title}'

    text_content = (
        f'Author: {instance.author.user}\n'
        f'Post: {instance.title}\n'
        f'http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'{instance.title}<br>'
        f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
    )
    
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.send()