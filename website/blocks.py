from django.utils.safestring import mark_safe
from django.utils.html import format_html
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from flex.blocks import FlexItemBlock, FlexContainerBlock
from flexcomponents.blocks import (
    FlexComponentContainerBlock, FlexMediaStreamBlock, FlexContentStreamBlock,
    FlexOverlayStreamBlock, FlexComponentStreamBlock
)
from wagtail.api import APIField
from wagtailmedia.blocks import AbstractMediaChooserBlock

# People/Leadership ============================================================

class PersonBlock(blocks.StructBlock):
    """A collection of blocks which define a Person"""
    image = ImageChooserBlock()
    name = blocks.CharBlock()
    title = blocks.CharBlock()
    bio = blocks.RichTextBlock()
    featured = blocks.BooleanBlock(
        required=False,
        help_text='Select to display this person more prominently'
    )

    class Meta:
        icon = 'user'
        label = 'Person'


class PersonStreamBlock(blocks.StreamBlock):
    """A StreamBlock wrapper for PersonBlock for use within a StreamField"""
    person = PersonBlock()

    class Meta:
        icon = 'user'
        label = 'Person'


class LeadershipGridBlock(blocks.StaticBlock):
    class Meta:
        icon = 'group'
        template = 'website/leadership_grid.html'
        label = 'Leadership Grid'
        admin_text = mark_safe('<hr/><b>{label}</b><hr/>'.format(label=label))


# Clients ======================================================================

class ClientBlock(blocks.StructBlock):
    """A collection of blocks which define a Client"""
    logo = ImageChooserBlock()
    name = blocks.CharBlock()

    class Meta:
        icon = 'user'
        label = 'Client'


class ClientStreamBlock(blocks.StreamBlock):
    """A StreamBlock wrapper for ClientBlock"""

    client = ClientBlock()

    class Meta:
        icon = 'user'
        label = 'Client'


class ClientsGridBlock(blocks.StaticBlock):
    class Meta:
        icon = 'group'
        template = 'website/clients_grid.html'
        label = 'Client Grid'
        admin_text = mark_safe('<hr/><b>{label}</b><hr/>'.format(label=label))


# Contact ======================================================================

class GoogleMapBlock(blocks.StructBlock):
    """Google Map struct block"""
    class Meta:
        template = 'website/google_map.html'
        label = 'Google Map'
        admin_text = mark_safe('<hr/><b>{label}</b><hr/>'.format(label=label))


class GoogleMapFlexBlock(FlexItemBlock):
    """Flex block for Google Map struct block"""
    content = GoogleMapBlock()

    class Meta:
        icon = 'site'
        verbose_name = 'Google Map'


class FlexGoogleMapStreamBlock(blocks.StreamBlock):
    """Stream block with extended media components for the Contact Page"""
    _OTHER_GROUP = 'Other'
    google_map = GoogleMapFlexBlock(group=_OTHER_GROUP)


# Flex Component overrides to include the Google Map block as a FlexItem

class ContactFlexComponentStreamBlock(FlexOverlayStreamBlock, FlexMediaStreamBlock, FlexContentStreamBlock, FlexGoogleMapStreamBlock):
    """StreamBlock with Wagtail foundation component flex blocks plus the Google Map flex block"""
    pass

class ContactFlexComponentContainerBlock(FlexComponentContainerBlock):
    flex_items = ContactFlexComponentStreamBlock()


# Looping video with lazy loading ==============================================

class LoopingLazyVideoChooserBlock(AbstractMediaChooserBlock):
    """Media chooser block for lazy looping videos"""
    def render_basic(self, value, context=None):
        if not value.type == 'video':
            return ''

        player_code = '''
        <video class="fluid-video lazy" playsinline autoplay muted loop>
        <source src="" type="video/mp4" data-src="{0}">
        </video>
        '''

        return format_html(player_code, value.file.url)

    class Meta:
        icon = 'media'


# Tinder Page ==================================================================

class TinderAttributeLogoChoiceBlock(blocks.ChoiceBlock):
    """Choice block with classes for different icon paths"""
    choices = [
        ('location', 'location'),
        ('occupation', 'occupation'),
        ('education', 'education'),
        ('interests', 'interests'),
        ('bio', 'bio'),
    ]

    class Meta:
        default = None
        required = False
        icon = 'arrows-up-down'


class TinderAttributeBlock(blocks.StructBlock):
    attribute_icon = ImageChooserBlock()
    text = blocks.CharBlock()

    class Meta:
        template = 'website/tinder_attribute.html'


# Work Sample Grid =============================================================

class _WorkSampleStaticBlock(blocks.StaticBlock):
    """Used to display admin text for WorkSampleGridBlock.

    Was having issues trying to use WorkSampleGridBlock as a StaticBlock, so
    instead this block serves to display admin text while avoiding strange
    template behavior
    """

    class Meta:
        verbose_name = 'Work Sample Grid'
        label = verbose_name
        icon = 'grip'
        admin_text = mark_safe(
            '<hr/><i>{info}</i><hr/>'.format(
                info='Grid of Work Sample Pages that are children of the current page.'
            )
        )


class WorkSampleGridBlock(blocks.StructBlock):
    """Shows a grid of preview images and text for all WorkSamplePage instances
    that are children of the current page
    """
    # Admin text
    work_sample_grid = _WorkSampleStaticBlock()

    class Meta:
        icon = 'grip'
        template = 'website/blocks/work_sample_grid.html'


class WorkSampleGridFlexBlock(FlexItemBlock):
    """Flex item for WorkSampleGridBlock"""
    content = WorkSampleGridBlock()

    class Meta:
        label = 'Work Sample Grid'
        verbose_name = label
        icon = 'grip'


# SCC Flex Component Containers ================================================

class SCCFlexComponentStreamBlock(FlexComponentStreamBlock):
    """Extended FlexComponentStreamBlock with custom components specific to the
    SCC site
    """
    _SCC_GROUP = 'SCC'
    work_sample_grid = WorkSampleGridFlexBlock(group=_SCC_GROUP)

class SCCFlexComponentContainerBlock(FlexComponentContainerBlock):
    """FlexComponentContainerBlock using SCCFlexComponentStreamBlock for its
    flex items
    """
    flex_items = SCCFlexComponentStreamBlock()

