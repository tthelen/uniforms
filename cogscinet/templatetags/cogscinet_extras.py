from django import template
from cogscinet.models import Verein
from django.db.models import Sum

register = template.Library()

@register.simple_tag
def total():
    total = 0
    for appl in Verein.objects.filter(validated=True):
        total += appl.fee()
    return "{} €".format(total)