from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(user_email, booking_details):
    subject = "Booking Confirmation"
    message = f"Dear customer, your booking has been confirmed!\n\n{booking_details}"
    send_mail(subject, message, 'no-reply@travelapp.com', [user_email])

