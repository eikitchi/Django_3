from django import template
from skychimp.models import Sending
register = template.Library()


@register.simple_tag
def sending_count():
    count = Sending.objects.all().count()
    return f'{count} рассылки'