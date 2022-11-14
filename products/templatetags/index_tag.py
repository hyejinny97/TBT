from django import template

register = template.Library()

@register.filter
def discount(value, sale):
    return int(int(value) * (100 - int(sale)) * 0.01)
