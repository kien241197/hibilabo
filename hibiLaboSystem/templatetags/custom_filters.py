from django import template

register = template.Library()

@register.filter(name='get_custom_name')
def get_custom_name(obj, attribute_name):
    return getattr(obj, attribute_name, '')