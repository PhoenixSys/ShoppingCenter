from django.template import Library

register = Library()


@register.filter
def space_to_underline(value):
    return value.replace(" ", "_")


@register.filter
def underline_to_space(value):
    return value.replace("_", " ")
