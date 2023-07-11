from django import template
from django.conf import settings


register = template.Library()


@register.simple_tag
def mediapath(image):
    return f"{settings.MEDIA_URL}{image}"