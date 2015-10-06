from django import template

register = template.Library()

# Turns an integer into a character starting
# with capital A
@register.filter
def label(value):
    return chr(value + 65)