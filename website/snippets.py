from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel

@register_snippet
class Client(models.Model):
	logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
	name = models.CharField(max_length=255, blank=True)
	
	panels = [
		FieldPanel('name'),
		ImageChooserPanel('logo'),
	]

	def __str__(self):
		return self.name