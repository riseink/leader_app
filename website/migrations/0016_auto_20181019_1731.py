# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-19 17:31
from __future__ import unicode_literals

import base.blocks.breaks
import base.blocks.headings
from django.db import migrations
import mediatext.blocks.videocopy
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_auto_20181018_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField((('flex_container', wagtail.core.blocks.StructBlock((('container_height', wagtail.core.blocks.ChoiceBlock(choices=[(None, 'Automatic'), ('flex-xs', 'Extra Small -- 20% of viewport'), ('flex-sm', 'Small -- 40% of viewport'), ('flex-md', 'Medium -- 50% of viewport'), ('flex-lg', 'Large -- 80% of viewport'), ('flex-xl', 'Extra Large -- 100% of viewport')], required=False)), ('animation_choice', wagtail.core.blocks.ChoiceBlock(choices=[(None, 'None'), ('primary', 'Primary Animation'), ('secondary', 'Secondary Animation'), ('tertiary', 'Tertiary Animation')], required=False)), ('container_classes', wagtail.core.blocks.ListBlock(wagtail.snippets.blocks.SnippetChooserBlock('flex.ContainerCSSClasses', label='Container CSS Classes', required=False), label='(Optional) Additional Container CSS Classes', required=False)), ('flex_items', wagtail.core.blocks.StreamBlock((('content', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock(group='Content')), ('headline', base.blocks.headings.H2Block(group='Content')), ('subtitle', base.blocks.headings.H3Block(group='Content')), ('description', wagtail.core.blocks.RichTextBlock(group='Content')), ('call_to_action', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False)), ('new_tab', wagtail.core.blocks.BooleanBlock(help_text='Open link in a new tab', required=False))), group='Buttons', label='Button (Link)')), ('email_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_email', wagtail.core.blocks.EmailBlock()), ('new_tab', wagtail.core.blocks.BooleanBlock(default=True, help_text='Open mailto link in a new tab', required=False))), group='Buttons', label='Button (Email Link)')), ('button_group', wagtail.core.blocks.StreamBlock((('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False)), ('new_tab', wagtail.core.blocks.BooleanBlock(help_text='Open link in a new tab', required=False))), label='Link Button')), ('email_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_email', wagtail.core.blocks.EmailBlock()), ('new_tab', wagtail.core.blocks.BooleanBlock(default=True, help_text='Open mailto link in a new tab', required=False)))))), group='Buttons')), ('horizontal_rule', base.blocks.breaks.HorizontalRuleBlock(group='Misc')))))), group='Content')), ('contact', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(required=False)), ('address', wagtail.core.blocks.RichTextBlock(required=False)), ('email', wagtail.core.blocks.CharBlock(required=False)), ('phone', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('Phone', wagtail.core.blocks.CharBlock()))))))))), group='Content')), ('tabbed_content', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StreamBlock((('content_tab', wagtail.core.blocks.StructBlock((('tab_text', wagtail.core.blocks.CharBlock(max_length=255)), ('content', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock(group='Content')), ('headline', base.blocks.headings.H2Block(group='Content')), ('subtitle', base.blocks.headings.H3Block(group='Content')), ('description', wagtail.core.blocks.RichTextBlock(group='Content')), ('call_to_action', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False)), ('new_tab', wagtail.core.blocks.BooleanBlock(help_text='Open link in a new tab', required=False))), group='Buttons', label='Button (Link)')), ('email_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_email', wagtail.core.blocks.EmailBlock()), ('new_tab', wagtail.core.blocks.BooleanBlock(default=True, help_text='Open mailto link in a new tab', required=False))), group='Buttons', label='Button (Email Link)')), ('button_group', wagtail.core.blocks.StreamBlock((('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False)), ('new_tab', wagtail.core.blocks.BooleanBlock(help_text='Open link in a new tab', required=False))), label='Link Button')), ('email_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_email', wagtail.core.blocks.EmailBlock()), ('new_tab', wagtail.core.blocks.BooleanBlock(default=True, help_text='Open mailto link in a new tab', required=False)))))), group='Buttons')), ('horizontal_rule', base.blocks.breaks.HorizontalRuleBlock(group='Misc')))))))),)))), group='Content')), ('tab_filter', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('unfiltered_tab_text', wagtail.core.blocks.CharBlock(help_text='Text to display on the unfiltered tab (default text: All)', max_length=255, required=False)), ('filtered_content', wagtail.core.blocks.StreamBlock((('filtered_content', wagtail.core.blocks.StructBlock((('tab_text', wagtail.core.blocks.CharBlock(help_text='Text to display on the filter tab', max_length=255)), ('content', wagtail.core.blocks.StreamBlock((('content', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock(group='Content')), ('headline', base.blocks.headings.H2Block(group='Content')), ('subtitle', base.blocks.headings.H3Block(group='Content')), ('description', wagtail.core.blocks.RichTextBlock(group='Content')), ('call_to_action', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False)), ('new_tab', wagtail.core.blocks.BooleanBlock(help_text='Open link in a new tab', required=False))), group='Buttons', label='Button (Link)')), ('email_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_email', wagtail.core.blocks.EmailBlock()), ('new_tab', wagtail.core.blocks.BooleanBlock(default=True, help_text='Open mailto link in a new tab', required=False))), group='Buttons', label='Button (Email Link)')), ('button_group', wagtail.core.blocks.StreamBlock((('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False)), ('new_tab', wagtail.core.blocks.BooleanBlock(help_text='Open link in a new tab', required=False))), label='Link Button')), ('email_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_email', wagtail.core.blocks.EmailBlock()), ('new_tab', wagtail.core.blocks.BooleanBlock(default=True, help_text='Open mailto link in a new tab', required=False)))))), group='Buttons')), ('horizontal_rule', base.blocks.breaks.HorizontalRuleBlock(group='Misc'))))),), help_text='Content to apply this filter to'))))),), help_text='Filter tabs and the content it applies to')))))), group='Content')), ('media_copy', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('background', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock(group='Content')), ('headline', base.blocks.headings.H2Block(group='Content')), ('subtitle', base.blocks.headings.H3Block(group='Content')), ('description', wagtail.core.blocks.RichTextBlock(group='Content')), ('call_to_action', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False)), ('new_tab', wagtail.core.blocks.BooleanBlock(help_text='Open link in a new tab', required=False))), group='Buttons', label='Button (Link)')), ('email_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_email', wagtail.core.blocks.EmailBlock()), ('new_tab', wagtail.core.blocks.BooleanBlock(default=True, help_text='Open mailto link in a new tab', required=False))), group='Buttons', label='Button (Email Link)')), ('button_group', wagtail.core.blocks.StreamBlock((('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False)), ('new_tab', wagtail.core.blocks.BooleanBlock(help_text='Open link in a new tab', required=False))), label='Link Button')), ('email_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_email', wagtail.core.blocks.EmailBlock()), ('new_tab', wagtail.core.blocks.BooleanBlock(default=True, help_text='Open mailto link in a new tab', required=False)))))), group='Buttons')), ('horizontal_rule', base.blocks.breaks.HorizontalRuleBlock(group='Misc'))))))))), group='Media')), ('looping_video_copy', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('background', mediatext.blocks.videocopy.LoopingVideoChooserBlock()), ('content', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock(group='Content')), ('headline', base.blocks.headings.H2Block(group='Content')), ('subtitle', base.blocks.headings.H3Block(group='Content')), ('description', wagtail.core.blocks.RichTextBlock(group='Content')), ('call_to_action', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False)), ('new_tab', wagtail.core.blocks.BooleanBlock(help_text='Open link in a new tab', required=False))), group='Buttons', label='Button (Link)')), ('email_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_email', wagtail.core.blocks.EmailBlock()), ('new_tab', wagtail.core.blocks.BooleanBlock(default=True, help_text='Open mailto link in a new tab', required=False))), group='Buttons', label='Button (Email Link)')), ('button_group', wagtail.core.blocks.StreamBlock((('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False)), ('new_tab', wagtail.core.blocks.BooleanBlock(help_text='Open link in a new tab', required=False))), label='Link Button')), ('email_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_email', wagtail.core.blocks.EmailBlock()), ('new_tab', wagtail.core.blocks.BooleanBlock(default=True, help_text='Open mailto link in a new tab', required=False)))))), group='Buttons')), ('horizontal_rule', base.blocks.breaks.HorizontalRuleBlock(group='Misc'))))))))), group='Media')), ('media_collection', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StreamBlock((('media_items', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.core.blocks.StreamBlock((('heading', base.blocks.headings.H4Block()), ('subheading', base.blocks.headings.H5Block()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False)), ('new_tab', wagtail.core.blocks.BooleanBlock(help_text='Open link in a new tab', required=False))))))))))),)))), group='Media')), ('carousel', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('carousel_height', wagtail.core.blocks.ChoiceBlock(choices=[(None, 'Automatic'), ('carousel-xs', 'Extra Small -- 20% of viewport'), ('carousel-sm', 'Small -- 40% of viewport'), ('carousel-md', 'Medium -- 50% of viewport'), ('carousel-lg', 'Large -- 80% of viewport'), ('carousel-xl', 'Extra Large -- 100% of viewport')], required=False)), ('carousel_type', wagtail.core.blocks.ChoiceBlock(choices=[(None, 'Simple'), ('tabbed', 'Tabbed'), ('split', 'Split')], required=False)), ('slides', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('slide_title', wagtail.core.blocks.CharBlock(help_text='Display name for the slide', required=False)), ('content', wagtail.core.blocks.StructBlock((('background', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock(group='Content')), ('headline', base.blocks.headings.H2Block(group='Content')), ('subtitle', base.blocks.headings.H3Block(group='Content')), ('description', wagtail.core.blocks.RichTextBlock(group='Content')), ('call_to_action', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False)), ('new_tab', wagtail.core.blocks.BooleanBlock(help_text='Open link in a new tab', required=False))), group='Buttons', label='Button (Link)')), ('email_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_email', wagtail.core.blocks.EmailBlock()), ('new_tab', wagtail.core.blocks.BooleanBlock(default=True, help_text='Open mailto link in a new tab', required=False))), group='Buttons', label='Button (Email Link)')), ('button_group', wagtail.core.blocks.StreamBlock((('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False)), ('new_tab', wagtail.core.blocks.BooleanBlock(help_text='Open link in a new tab', required=False))), label='Link Button')), ('email_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_email', wagtail.core.blocks.EmailBlock()), ('new_tab', wagtail.core.blocks.BooleanBlock(default=True, help_text='Open mailto link in a new tab', required=False)))))), group='Buttons')), ('horizontal_rule', base.blocks.breaks.HorizontalRuleBlock(group='Misc')))))))))))))))), group='Media')), ('iframe', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('iframe_height', wagtail.core.blocks.ChoiceBlock(choices=[(None, 'Automatic'), ('iframe-xs', 'Extra Small -- 20% of viewport'), ('iframe-sm', 'Small -- 40% of viewport'), ('iframe-md', 'Medium -- 50% of viewport'), ('iframe-lg', 'Large -- 80% of viewport'), ('iframe-xl', 'Extra Large -- 100% of viewport')], required=False)), ('iframe_url', wagtail.core.blocks.URLBlock(label='Source URL', required=True)))))), group='Media')), ('vimeo_player', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('height', wagtail.core.blocks.ChoiceBlock(choices=[('xs', 'Extra Small -- 20% of viewport'), ('sm', 'Small -- 40% of viewport'), ('md', 'Medium -- 50% of viewport'), ('lg', 'Large -- 80% of viewport'), ('xl', 'Extra Large -- 100% of viewport')])), ('video_link', wagtail.core.blocks.CharBlock(help_text='The Vimeo ID for the video', label='Video ID', required=True)), ('video', wagtailmedia.blocks.AbstractMediaChooserBlock(help_text='(Optional) Teaser video to use as a background', label='Preview video', required=False)), ('poster_image', wagtail.images.blocks.ImageChooserBlock(help_text='(Optional) Background image that displays while preview video is loading or in place of a preview video if none is specified', required=False)), ('headline', wagtail.core.blocks.RichTextBlock(required=False)), ('cta_copy', wagtail.core.blocks.CharBlock(help_text='(Optional) Play button text. Will use a play icon instead of text if unspecified', label='Play button text', required=False)), ('expanding', wagtail.core.blocks.BooleanBlock(help_text='If checked, video player will expand when clicked rather than constraining the video height', label='Expanding video player', required=False)))))), group='Media')), ('overlay_button', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('overlay', wagtail.snippets.blocks.SnippetChooserBlock('overlay.Overlay')), ('trigger', wagtail.core.blocks.CharBlock(label='Button Text', max_length=255)))))), group='Overlays')), ('overlay_image', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('overlay', wagtail.snippets.blocks.SnippetChooserBlock('overlay.Overlay')), ('trigger', wagtail.images.blocks.ImageChooserBlock(label='Image')))))), group='Overlays')), ('overlay_gallery', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('show_arrows', wagtail.core.blocks.BooleanBlock(default=True, help_text='If checked, overlay will have arrows to cycle to the previous/next image in the gallery', label='Show previous/next arrows', required=False)), ('images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('content', wagtail.core.blocks.RichTextBlock(blank=True, required=False)))))))))), group='Overlays')), ('popup', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('mp_button_text', wagtail.core.blocks.CharBlock(label='Button Text', max_length=255)), ('mp_button_href', wagtail.core.blocks.PageChooserBlock(label='Popup Content')))))), group='Overlays')), ('social_media_post_gallery', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('show_arrows', wagtail.core.blocks.BooleanBlock(default=True, help_text='If checked, overlay will have arrows to cycle to the previous/next image in the gallery', label='Show previous/next arrows', required=False)), ('images', wagtail.core.blocks.StreamBlock((('instagram', wagtail.core.blocks.StructBlock((('post', wagtail.snippets.blocks.SnippetChooserBlock('socialmedia.InstagramPost')),))), ('generic', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('content', wagtail.core.blocks.RichTextBlock(blank=True, required=False))), label='Generic Post (Image)'))), label='Social Media Posts')))))), group='Overlays')))))))),), blank=True),
        ),
    ]
