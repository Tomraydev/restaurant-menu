from datetime import datetime, timedelta

from api.models import Dish
from config.celery import app
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Q
from django.template.loader import render_to_string


@app.task()
def send_email_notifications(test=False):
    """
    Send an email with all dishes added/modified yesterday.
    (!) Turned off during development
    """
    yesterday = (datetime.now() - timedelta(1)).strftime("%Y-%m-%d")
    dishes = Dish.objects.all()
    dishes = dishes.filter(Q(date_added=yesterday) | Q(date_modified=yesterday))

    if dishes:
        email_subject = "Nowe przepisy w naszej restauracji!"
        for user in User.objects.all():
            message = render_to_string("new_dishes_mail_template.html", {"user": user, "dishes": dishes})
            # send_mail(email_subject, message, "admin@restaurant-menu.com", [user.email], fail_silently=False,) # (!) Turned off during development
    if test:
        user = User.objects.all().filter(username="admin")[0]
        message = render_to_string("new_dishes_mail_template.html", {"user": user, "dishes": dishes})
        return message
