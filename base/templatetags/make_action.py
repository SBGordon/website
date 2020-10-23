from django import template
register = template.Library()

@register.simple_tag
def set_var(foo):
    return foo
    
@register.simple_tag    
def set_int(num):
     return int(num)
    
@register.simple_tag
def aggregator(var, num):
    return str(int(var) + num)
    
