from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives

from .models import Response, User


@receiver(post_save,   sender=Response)
def comment_created(instance, created, **kwargs):
    if not created:
        return

    post = instance.post
    post_author = post.author
    author = instance.author
    comment = instance.text
        
        
    subject = f'New Comment:'

    text_content = (
        f'New comment from {author.username}\n'
        f'{comment}\n'
        f'http://127.0.0.1:8000/mmorpg/comments/'
    )
    html_content = (
        f'New comment from - {author.username}<br>'
        f'---- {comment} ---- <br>'
        f'http://127.0.0.1:8000/mmorpg/comments/'
    )
    
    msg = EmailMultiAlternatives(subject, text_content, None, [post_author.email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
