from django.core.management import BaseCommand
from skychimp.services import send_email
from skychimp.models import *

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        send_email(Sending.ONCE)