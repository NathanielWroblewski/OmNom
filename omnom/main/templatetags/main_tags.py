from django import template

register = template.Library()

def get_range(value):
    return range(value)

register.filter("get_range",get_range)
