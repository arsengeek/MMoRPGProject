from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives

from .models import Response, User


@receiver(post_save,   sender=Response)
def subscriptions_post_created(instance, created, **kwargs):
    if not created:
        return

    post = instance.post
    post_author = post.author
    author = instance.author
    comment = instance.text
        
        
    subject = f'New post: {instance.title}'

    text_content = (
        f'New comment from {author.username}'
        f'{comment}'
        f'http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'{instance.title}<br>'
        f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
    )
    
    msg = EmailMultiAlternatives(subject, text_content, None, [post_author.email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
