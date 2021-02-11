import datetime

from django import template

register = template.Library()


@register.filter
def format_date(value):
    value = datetime.datetime.strptime(value, "%Y-%m-%d")
    # value = value.strftime('%d/%m/%y')
    return value
