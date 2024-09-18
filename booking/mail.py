from django.core.mail import send_mail
from django.conf import settings

def send_email_notification(subject, message, to_email, from_email=None):
    subject = subject
    message = message
    to_email = to_email
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, to_email)