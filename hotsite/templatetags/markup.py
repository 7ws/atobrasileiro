from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from markdown import markdown


register = template.Library()


@register.filter('markdown')
@stringfilter
def markdown_to_html(text):
    return mark_safe(markdown(text))
