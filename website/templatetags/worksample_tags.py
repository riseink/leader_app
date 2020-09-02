from django import template
from wagtail.core.models import Page

from website.models import WorkSamplePage


register = template.Library()

@register.inclusion_tag('website/tags/work_sample_grid.html', takes_context=True)
def work_sample_grid(context, parent):
    """Renders a work sample preview grid using all WorkSamplePage instances
    that are children of the specified parent

    :param context:
    :param parent:
    """
    work_samples = Page.objects.child_of(parent).live().exact_type(WorkSamplePage).specific()
    return {
        'work_samples': work_samples,
        'request': context['request'],
    }

