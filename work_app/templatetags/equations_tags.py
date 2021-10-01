from django import template

from work_app.equations_data import equations


register = template.Library()


@register.simple_tag()
def get_equations_list():
    return equations