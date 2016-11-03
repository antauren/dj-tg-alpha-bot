from django import template
from django.http import QueryDict
register = template.Library()


@register.filter(name='keyboard_field')
def keyboard_field(value, args=None):
    """
    Format keyboard /command field.
    """
    def convert(element, joiner=" "):
        """Join with joiner values of element's fields."""
        joined_fields = joiner.join(str(getattr(element, field))
                                    for field
                                    in fields)
        return "/" + command + " " + joined_fields

    def group(flat, size):
        return [flat[i: i + size] for i in range(0, len(flat), size)]

    qs = QueryDict(args)
    per_line = qs.get('per_line', 1)
    fields = qs.getlist("field", ["slug"])
    # field = qs.get("field", "slug")
    command = qs.get("command")
    grouped = group(value, int(per_line))
    new_list = []
    for line in grouped:
        new_list.append([convert(e) for e in line])
    return str(new_list).encode('utf-8')
