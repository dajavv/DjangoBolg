from django.template import Library

register = Library()


@register.filter
def md(value):  # 过滤器
    import markdown
    return markdown.markdown(value)
