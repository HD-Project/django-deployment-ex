from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cut all value of the string
    """
    return value.replace(arg,'')

# register.filter('cut',cut)



