from django import template

register = template.Library()

@register.simple_tag(name='title_text')
def title_text(text):
    begin = text.find('<p>') + 3
    end = text.find("</p>")
    if end > (begin + 150):
        end = begin + 150
    new_text = text[begin:end]
    if new_text[-2] == '.':
        return new_text[:-1]
    elif new_text[-1] == '.':
        return new_text
    else:
        new_text = text[begin:end] + '...'
        return new_text
