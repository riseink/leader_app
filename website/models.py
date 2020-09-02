import json
from random import randint

from django.db import models
from django.forms import FileField
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.core.serializers.json import DjangoJSONEncoder
from django.conf import settings
from modelcluster.fields import ParentalKey

from wagtail.api import APIField
from wagtail.core import blocks
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField, RichTextField
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import (
    StreamFieldPanel, FieldPanel, FieldRowPanel, MultiFieldPanel, PageChooserPanel, InlinePanel
)
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField, FORM_FIELD_CHOICES
from wagtail.contrib.forms.forms import FormBuilder
from wagtail.admin.utils import send_mail
from wagtail.documents.models import get_document_model


class HomePage(Page):
    pass