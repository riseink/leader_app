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


from flexcomponents.blocks import FlexComponentContainerBlock
from flexcomponents.models import FlexLayoutFields
from mediatext.blocks import LoopingVideoChooserBlock
from carousel.blocks import CarouselFlexBlock

from website.base.serializers import APIRichTextSerializer

from website.blocks import (
    PersonStreamBlock, LeadershipGridBlock, TinderAttributeBlock,
    ClientStreamBlock, ClientsGridBlock, ContactFlexComponentContainerBlock,
    SCCFlexComponentContainerBlock, LoopingLazyVideoChooserBlock,
)

from website.snippets import Client

# Flex Layout Fields ===========================================================

class SCCFlexLayoutFields(FlexLayoutFields):
    """Extended FlexLayoutFields with additional custom flex components from
    SCCFlexComponentContainerBlock
    """
    body = StreamField([
        ('flex_container', SCCFlexComponentContainerBlock()),
    ], blank=True)

    class Meta:
        abstract = True


# Home Page ====================================================================

class HomePage(SCCFlexLayoutFields, Page):
    """HomePage model with FlexLayoutPage fields"""

    """ Get the number of intro videos """
    def __set_video_count(self):
        self.__video_count = self.intro_videos.aggregate(count=models.aggregates.Count('id'))['count']

    """ Get a random index from the video count """
    def __get_random(self):
        return randint(0, self.__video_count - 1)

    """ Get the intro video """
    def get_first_intro_video(self):
        self.__set_video_count()
        return self.intro_videos.all()[self.__get_random()]


    api_fields = [
        APIField('intro_videos')
    ]


    content_panels = SCCFlexLayoutFields.content_panels + [
        InlinePanel('intro_videos', label='Intro Videos'),
        InlinePanel('featured_work_samples', label="Featured Work Samples")
    ]


class HomeIntroVideos(Orderable):
    """Model for home page intro videos"""
    page = ParentalKey(HomePage, related_name='intro_videos')

    video_block = StreamField([('video', LoopingVideoChooserBlock())])
    video_block_portrait = StreamField([('video', LoopingVideoChooserBlock())], blank=True)
    video_block_landscape = StreamField([('video', LoopingVideoChooserBlock())], blank=True)

    api_fields = [
        APIField('video_block', serializer=APIRichTextSerializer()),
        APIField('video_block_portrait', serializer=APIRichTextSerializer()),
        APIField('video_block_landscape', serializer=APIRichTextSerializer()),
    ]

    panels = [
        StreamFieldPanel('video_block'),
        StreamFieldPanel('video_block_portrait'),
        StreamFieldPanel('video_block_landscape'),
    ]


class FeaturedWorkSamples(Orderable):
    """Model for featured work samples on the home page"""
    page = ParentalKey(HomePage, related_name='featured_work_samples')
    work_sample = models.ForeignKey(
        'website.WorkSamplePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        # only allow WorkSamplePages
        PageChooserPanel('work_sample', 'website.WorkSamplePage')
    ]

# Work Index Page
class WorkPage(SCCFlexLayoutFields, Page):
    pass

# Work Sample Pages

class WorkSamplePage(SCCFlexLayoutFields, Page):
    """Work Sample Page model with FlexLayoutPage fields"""
    ghost_page = models.BooleanField(
        default=False,
        help_text="If checked, this page will be hidden throughout the site, but will remain accessible via its URL."
    )
    client = models.ForeignKey(
        'website.Client',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    work_title = models.CharField(max_length=255, blank=True)
    intro_text = StreamField([
        ('introduction', FlexComponentContainerBlock())
    ], blank=True)
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    featured_video = StreamField([
        ('looping_video', LoopingVideoChooserBlock()),
        ('looping_lazy_video', LoopingLazyVideoChooserBlock()),
    ], blank=True)

    def get_next_active_sibling(self):
        siblings = WorkSamplePage.objects.sibling_of(self).live().filter(ghost_page=False)
        next_siblings = siblings.filter(path__gt=self.path)
        if next_siblings:
            return next_siblings.first()
        else:
            return siblings.first()

    def get_prev_active_sibling(self):
        siblings = WorkSamplePage.objects.sibling_of(self).live().filter(ghost_page=False)
        prev_siblings = siblings.filter(path__lt=self.path)
        if prev_siblings:
            return prev_siblings.last()
        else:
            return siblings.last()

    advanced_settings_panel = [
        MultiFieldPanel([
            FieldPanel('ghost_page'),
            SnippetChooserPanel('client'),
            FieldPanel('work_title'),
            StreamFieldPanel('intro_text'),
            ImageChooserPanel('featured_image'),
            StreamFieldPanel('featured_video')
        ], heading='Advanced Settings', classname='collapsible'),
    ]

    def client_logo(self):
        return self.client.logo

    content_panels = SCCFlexLayoutFields.content_panels + advanced_settings_panel



# Leadership Page, People Settings

@register_setting(icon='user')
class PeopleSettings(BaseSetting):
    """A setting used for managing people, which populate the Leadership page. Each
    Person has a name, title, biography, and image.
    """
    person = StreamField(PersonStreamBlock())

    panels = [
        StreamFieldPanel('person'),
    ]

    class Meta:
        verbose_name = 'Leadership'


class LeadershipPage(SCCFlexLayoutFields, Page):
    """Leadership Page model -- extension of FlexLayoutPage, with additional StreamBlock
    for Leadership Grid
    """
    body = StreamField([
        ('flex_container', FlexComponentContainerBlock()),
        ('leadership_grid', LeadershipGridBlock())
    ], blank=True)



# About Page

class AboutPage(SCCFlexLayoutFields, Page):
    """About Page model -- extension of FlexLayoutPage, with additional StreamBlock
    for Client Grid
    """
    body = StreamField([
        ('flex_container', FlexComponentContainerBlock()),
        ('client_grid', ClientsGridBlock()),
    ], blank=True)

    content_panels = SCCFlexLayoutFields.content_panels + [
        InlinePanel('clients', label="Clients")
    ]


class ClientGrid(Orderable):
    """Model for home page intro videos"""
    page = ParentalKey(AboutPage, related_name='clients')

    client = models.ForeignKey(
        'website.Client',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        SnippetChooserPanel('client')
    ]


# Contact Page

class ContactPage(SCCFlexLayoutFields, Page):
    """Contact Page model -- extension of FlexLayoutPage, with a custom FlexComponentContainer
    that includes a Google Map stream block"""
    body = StreamField([
        ('flex_container', ContactFlexComponentContainerBlock())
    ], blank=True)
    pass


# Discipline Page
class DisciplinePage(SCCFlexLayoutFields, Page):
    hero_area = StreamField([
        ('hero_area', FlexComponentContainerBlock())
    ], blank=True)

    introduction = StreamField([
        ('introduction', FlexComponentContainerBlock())
    ], blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
                FieldPanel('show_navbar'),
                FieldPanel('show_footer'),
                StreamFieldPanel('announcements'),
            ], heading='Page Options', classname='collapsible'),
        StreamFieldPanel('hero_area'),
        InlinePanel('management', label='Management'),
        StreamFieldPanel('introduction'),
        StreamFieldPanel('body'),
    ]

class DisciplineManagers(Orderable):
    page = ParentalKey(DisciplinePage, related_name='management')

    name = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('title'),
        ImageChooserPanel('image'),
    ]

# News Pages
class NewsLandingPage(SCCFlexLayoutFields, Page):
    """News Landing page model"""
    def get_context(self, request):
        context = super(NewsLandingPage, self).get_context(request)
        all_news_pages = NewsPage.objects.live().order_by('-date')  # order by recently published
        context['news_pages'] = all_news_pages
        return context

class NewsPage(SCCFlexLayoutFields, Page):
    """News page model"""

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    headline = models.CharField(max_length=255)
    published_by = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True)
    article_url = models.URLField(null=True, blank=True, help_text="A link to the original article")
    # wrapped RichTextBlock in StreamField due to error caused by changing body to a non-StreamField
    body = StreamField([
        ('article_body', blocks.RichTextBlock(null=True, blank=True))
    ])

    content_panels = SCCFlexLayoutFields.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('headline'),
        FieldPanel('published_by'),
        FieldPanel('author'),
        FieldPanel('article_url'),
        FieldPanel('date'),
    ]

# Careers Page
class CareersPage(SCCFlexLayoutFields, Page):
    closing_content = StreamField([
        ('closing_content', FlexComponentContainerBlock())
    ], blank=True)

    content_panels = SCCFlexLayoutFields.content_panels + [
        StreamFieldPanel('closing_content'),
    ]


# Job Application Page
class JobDetailsPage(SCCFlexLayoutFields, Page):
    department = models.CharField(max_length=255)

    short_description = models.CharField(max_length=255, null=True, blank=True)

    application_form_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = Page.content_panels + [
        FieldPanel('department'),
        FieldPanel('short_description'),
        StreamFieldPanel('body'),
        PageChooserPanel('application_form_page', 'website.ApplicationFormPage'),
        MultiFieldPanel([
                FieldPanel('show_navbar'),
                FieldPanel('show_footer'),
                StreamFieldPanel('announcements'),
            ], heading='Page Options', classname='collapsible'),
    ]

    def form_page(self):
        return self.application_form_page.specific

class ApplicationFormField(AbstractFormField):
    CHOICES = FORM_FIELD_CHOICES + (('upload', 'Upload File'),)

    field_type = models.CharField(
        verbose_name='field type',
        max_length=16,
        choices=CHOICES)

    page = ParentalKey('ApplicationFormPage', on_delete=models.CASCADE, related_name='form_fields')

class ApplicationFormBuilder(FormBuilder):
    def create_upload_field(self, field, options):
        return FileField(**options)


class ApplicationFormPage(AbstractEmailForm):
    form_builder = ApplicationFormBuilder

    thank_you_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    def render_landing_page(self, request, form_submission=None, *args, **kwargs):
        if self.thank_you_page:
            url = self.thank_you_page.url
            return redirect(url, permanent=False)
        # if no thank_you_page is set, render default landing page
        return super().render_landing_page(request, form_submission, *args, **kwargs)


    def send_mail(self, form, attachments):
        # `self` is the FormPage, `form` is the form's POST data on submit

        # Email addresses are parsed from the FormPage's addresses field
        addresses = [x.strip() for x in self.to_address.split(',')]

        subject = self.subject + " - "  # add position email subject

        content = []

        for field in form:
            # add the value of each field as a new line
            value = field.value()
            if isinstance(value, list):
                value = ', '.join(value)
            content.append('{}: {}'.format(field.label, value))


        # Temporary fix to include link to uploads in the email text
        if attachments:
            for attachment in attachments:
                content.append('{}documents/{}'.format(settings.MEDIA_URL, attachment.filename))

        # Content is joined with a new line to separate each text line
        content = '\n'.join(content)


        email = EmailMessage(
            subject,
            content,
            self.from_address,
            addresses,
        )

        # if attachments:
        #     for attachment in attachments:
        #         email.attach(attachment.title, attachment.filename)

        email.send()


    def serve(self, request, *args, **kwargs):
        if request.method == 'POST':
            # form = self.get_form(request.POST, page=self, user=request.user)  # Original line
            form = self.get_form(request.POST, request.FILES, page=self, user=request.user)

            if form.is_valid():
                form_submission = self.process_form_submission(form)
                return self.render_landing_page(request, form_submission, *args, **kwargs)

        else:
            form = self.get_form(page=self, user=request.user)

        context = self.get_context(request)
        context['form'] = form
        return render(
            request,
            self.get_template(request),
            context
        )

    def process_form_submission(self, form):
        cleaned_data = form.cleaned_data
        attachments = []

        for name, field in form.fields.items():
            if isinstance(field, FileField):
                file_data = cleaned_data[name]
                if file_data:
                    DocumentModel = get_document_model()
                    document = DocumentModel(
                        file=file_data,
                        title=cleaned_data[name].name
                    )
                    document.save()

                    attachments.append(document)
                    cleaned_data.update({name: document.title})
                else:
                    # remove the value from the data
                    del cleaned_data[name]

        form_data = json.dumps(cleaned_data, cls=DjangoJSONEncoder)
        self.get_submission_class().objects.create(
            form_data=form_data,
            page=self,
        )

        if self.to_address:
            self.send_mail(form, attachments)


    def get_form_fields(self):
        return self.form_fields.all()


    content_panels = AbstractEmailForm.content_panels + [
        InlinePanel('form_fields', label="Form fields"),
        PageChooserPanel('thank_you_page'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

class TinderPage(SCCFlexLayoutFields, Page):
    """Tinder Page model -- extension of FlexLayoutPage"""

    tinder_image_carousel = StreamField([('carousel', CarouselFlexBlock())], blank=True)

    like_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    dislike_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    tinder_name = models.CharField(max_length=255)
    tinder_age = models.CharField(max_length=255)
    tinder_attributes = StreamField([('attributes', TinderAttributeBlock())], blank=True)

    content_panels = SCCFlexLayoutFields.content_panels + [
        MultiFieldPanel([
            StreamFieldPanel('tinder_image_carousel'),
            PageChooserPanel('like_page', 'wagtailcore.Page'),
            PageChooserPanel('dislike_page', 'wagtailcore.Page'),
            FieldPanel('tinder_name'),
            FieldPanel('tinder_age'),
            StreamFieldPanel('tinder_attributes'),
        ], heading="Tinder Profile")
    ]


# Site Settings ====================================================================

@register_setting(icon='image')
class AnimationSettings(BaseSetting):
    """Settings model with choices for primary, secondary, and tertiary
    animations
    """

    ANIMATION_CHOICES = [
        (None, 'None'),
        ('anim willFadeIn', 'Fade in'),
        ('anim willFadeFromTop', 'Fade in from top'),
        ('anim willFadeFromRight', 'Fade in from right'),
        ('anim willFadeFromBottom', 'Fade in from bottom'),
        ('anim willFadeFromLeft', 'Fade in from left'),
    ]

    primary_animation = models.CharField(
        max_length=25,
        choices=ANIMATION_CHOICES,
        default=None,
        null=True, blank=True
    )

    secondary_animation = models.CharField(
        max_length=25,
        choices=ANIMATION_CHOICES,
        default=None,
        null=True, blank=True
    )

    tertiary_animation = models.CharField(
        max_length=25,
        choices=ANIMATION_CHOICES,
        default=None,
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'Animations Settings'

