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

class UserPage(Page):

    TEAM1 = 'T1'
    TEAM2 = 'T2'
    TEAM3 = 'T3'
    TEAM4 = 'T4'
    TEAM5 = 'T5'
    TEAM6 = 'T6'
    TEAM7 = 'T7'
    TEAM8 = 'T8'
    TEAM9 = 'T9'
    TEAM10 = 'T10'
    TEAM11 = 'T11'
    TEAM12 = 'T12'
    TEAM13 = 'T13'
    TEAM14 = 'T14'
    TEAM15 = 'T15'
    TEAM16 = 'T16'
    TEAM17 = 'T17'
    TEAM18 = 'T18'
    TEAM19 = 'T19'
    TEAM20 = 'T20'
    TEAM21 = 'T21'
    TEAM22 = 'T22'
    TEAM23 = 'T23'
    TEAM24 = 'T24'
    TEAM25 = 'T25'
    TEAM_CHOICES = [
        (TEAM1, 'Team 1'),
        (TEAM2, 'Team 2'),
        (TEAM3, 'Team 3'),
        (TEAM4, 'Team 4'),
        (TEAM5, 'Team 5'),
        (TEAM6, 'Team 6'),
        (TEAM7, 'Team 7'),
        (TEAM8, 'Team 8'),
        (TEAM9, 'Team 9'),
        (TEAM10, 'Team 10'),
        (TEAM11, 'Team 11'),
        (TEAM12, 'Team 12'),
        (TEAM13, 'Team 13'),
        (TEAM14, 'Team 14'),
        (TEAM15, 'Team 15'),
        (TEAM16, 'Team 16'),
        (TEAM17, 'Team 17'),
        (TEAM18, 'Team 18'),
        (TEAM19, 'Team 19'),
        (TEAM20, 'Team 20'),
        (TEAM21, 'Team 21'),
        (TEAM22, 'Team 22'),
        (TEAM23, 'Team 23'),
        (TEAM24, 'Team 24'),
        (TEAM25, 'Team 25'),
    ]

    team_selection = models.CharField(
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=TEAM1,
    )
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    golf_handicap = models.IntegerField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)

