from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from .mail import send_email_notification

@receiver(post_save, sender=Reservation)
def my_handler(sender, instance, created, **kwargs):
    if created:
        subject = 'Booking Successfully Completed'
        message = f'Hello {instance.userName} Thank you for Booking'
        to_email = [instance.email]
        send_email_notification(subject, message, to_email)
    else:
        print('not working')
        