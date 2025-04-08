import datetime
from django import template
from django.utils.timezone import now

register = template.Library()

@register.filter
def humanized_date(value):
    if not value:
        return "No date"

    today = now().date()
    delta = (value - today).days

    if delta == 0:
        return "Today"
    elif delta == -1:
        return "Yesterday"
    elif delta < 0:
        return f"{abs(delta)} days ago"
    else:
        return f"In {delta} days"
