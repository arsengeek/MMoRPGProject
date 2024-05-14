from apscheduler.schedulers.background import BlockingScheduler
from MMoRPGapp.models import User
from django.core.mail import EmailMultiAlternatives
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings

def signals(*args, **options):
    users = User.objects.all()
    emails = [user.email for user in users]

    subject = 'News Today MMORPG'
    text_content = (
        'Hey bro, you play in our game, we congratulate you because you can be one of the first to find out news about our game\n'
        'http://127.0.0.1:8000/mmorpg/posts'
    )
    html_content = (
        'Hey bro, you play in our game, we congratulate you because you can be one of the first to find out news about our game <br>'
        "<img src='assets/mmorpg.jpg'></img>"
        'http://127.0.0.1:8000/mmorpg/posts'
    )

    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

class Command(BaseCommand):
    help = "Runs APScheduler."
    
    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), 'default')
        
        scheduler.add_job(
            signals,
            trigger=CronTrigger(second="*/10"),
            id="signals",
            max_instances=1,
            replace_existing=True,
        )
    
        try:
            scheduler.start()
        except KeyboardInterrupt:
            scheduler.shutdown()