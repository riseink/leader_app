# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-05 14:01
from __future__ import unicode_literals

import base.blocks.breaks
import base.blocks.headings
from django.db import migrations, models
import django.db.models.deletion
import mediatext.blocks.videocopy
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks
import wagtailmedia.blocks

import website.blocks
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('overlay', '0002_auto_20180925_2054'),
        ('website', '0011_merge_20181004_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadershipPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('show_navbar', models.BooleanField(default=True)),
                ('show_footer', models.BooleanField(default=True)),
                ('body', wagtail.core.fields.StreamField((('flex_container', wagtail.core.blocks.StructBlock((('container_height', wagtail.core.blocks.ChoiceBlock(choices=[(None, 'Automatic'), ('flex-xs', 'Extra Small -- 20% of viewport'), ('flex-sm', 'Small -- 40% of viewport'), ('flex-md', 'Medium -- 50% of viewport'), ('flex-lg', 'Large -- 80% of viewport'), ('flex-xl', 'Extra Large -- 100% of viewport')], required=False)), ('animation_choice', wagtail.core.blocks.ChoiceBlock(choices=[(None, 'None'), ('primary', 'Primary Animation'), ('secondary', 'Secondary Animation'), ('tertiary', 'Tertiary Animation')], required=False)), ('container_classes', wagtail.core.blocks.ListBlock(wagtail.snippets.blocks.SnippetChooserBlock('flex.ContainerCSSClasses', label='Container CSS Classes', required=False), label='(Optional) Additional Container CSS Classes', required=False)), ('flex_items', wagtail.core.blocks.StreamBlock((('media_copy', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('background', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('headline', base.blocks.headings.H2Block()), ('subtitle', base.blocks.headings.H3Block()), ('description', wagtail.core.blocks.RichTextBlock()), ('call_to_action', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))), ('button_group', wagtail.core.blocks.StreamBlock((('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))),))), ('horizontal_rule', base.blocks.breaks.HorizontalRuleBlock())))))))), group='Media')), ('looping_video_copy', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('background', mediatext.blocks.videocopy.LoopingVideoChooserBlock()), ('content', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('headline', base.blocks.headings.H2Block()), ('subtitle', base.blocks.headings.H3Block()), ('description', wagtail.core.blocks.RichTextBlock()), ('call_to_action', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))), ('button_group', wagtail.core.blocks.StreamBlock((('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))),))), ('horizontal_rule', base.blocks.breaks.HorizontalRuleBlock())))))))), group='Media')), ('media_collection', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StreamBlock((('media_items', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.core.blocks.StreamBlock((('heading', base.blocks.headings.H4Block()), ('subheading', base.blocks.headings.H5Block()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))))))))),)))), group='Media')), ('carousel', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('carousel_height', wagtail.core.blocks.ChoiceBlock(choices=[(None, 'Automatic'), ('carousel-xs', 'Extra Small -- 20% of viewport'), ('carousel-sm', 'Small -- 40% of viewport'), ('carousel-md', 'Medium -- 50% of viewport'), ('carousel-lg', 'Large -- 80% of viewport'), ('carousel-xl', 'Extra Large -- 100% of viewport')], required=False)), ('carousel_type', wagtail.core.blocks.ChoiceBlock(choices=[(None, 'Simple'), ('tabbed', 'Tabbed'), ('split', 'Split')], required=False)), ('slides', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('slide_title', wagtail.core.blocks.CharBlock(help_text='Display name for the slide', required=False)), ('content', wagtail.core.blocks.StructBlock((('background', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('headline', base.blocks.headings.H2Block()), ('subtitle', base.blocks.headings.H3Block()), ('description', wagtail.core.blocks.RichTextBlock()), ('call_to_action', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))), ('button_group', wagtail.core.blocks.StreamBlock((('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))),))), ('horizontal_rule', base.blocks.breaks.HorizontalRuleBlock()))))))))))))))), group='Media')), ('iframe', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('iframe_height', wagtail.core.blocks.ChoiceBlock(choices=[(None, 'Automatic'), ('iframe-xs', 'Extra Small -- 20% of viewport'), ('iframe-sm', 'Small -- 40% of viewport'), ('iframe-md', 'Medium -- 50% of viewport'), ('iframe-lg', 'Large -- 80% of viewport'), ('iframe-xl', 'Extra Large -- 100% of viewport')], required=False)), ('iframe_url', wagtail.core.blocks.URLBlock(label='Source URL', required=True)))))), group='Media')), ('vimeo_player', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('height', wagtail.core.blocks.ChoiceBlock(choices=[('xs', 'Extra Small -- 20% of viewport'), ('sm', 'Small -- 40% of viewport'), ('md', 'Medium -- 50% of viewport'), ('lg', 'Large -- 80% of viewport'), ('xl', 'Extra Large -- 100% of viewport')])), ('video_link', wagtail.core.blocks.CharBlock(help_text='The Vimeo ID for the video', label='Video ID', required=True)), ('video', wagtailmedia.blocks.AbstractMediaChooserBlock(help_text='(Optional) Teaser video to use as a background', label='Preview video', required=False)), ('poster_image', wagtail.images.blocks.ImageChooserBlock(help_text='(Optional) Background image that displays while preview video is loading or in place of a preview video if none is specified', required=False)), ('headline', wagtail.core.blocks.RichTextBlock(required=False)), ('cta_copy', wagtail.core.blocks.CharBlock(help_text='(Optional) Play button text. Will use a play icon instead of text if unspecified', label='Play button text', required=False)), ('expanding', wagtail.core.blocks.BooleanBlock(help_text='If checked, video player will expand when clicked rather than constraining the video height', label='Expanding video player', required=False)))))), group='Media')), ('content', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('headline', base.blocks.headings.H2Block()), ('subtitle', base.blocks.headings.H3Block()), ('description', wagtail.core.blocks.RichTextBlock()), ('call_to_action', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))), ('button_group', wagtail.core.blocks.StreamBlock((('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))),))), ('horizontal_rule', base.blocks.breaks.HorizontalRuleBlock()))))), group='Content')), ('contact', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(required=False)), ('address', wagtail.core.blocks.RichTextBlock(required=False)), ('email', wagtail.core.blocks.CharBlock(required=False)), ('phone', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('Phone', wagtail.core.blocks.CharBlock()))))))))), group='Content')), ('tabbed_content', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StreamBlock((('content_tab', wagtail.core.blocks.StructBlock((('tab_text', wagtail.core.blocks.CharBlock(max_length=255)), ('content', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('headline', base.blocks.headings.H2Block()), ('subtitle', base.blocks.headings.H3Block()), ('description', wagtail.core.blocks.RichTextBlock()), ('call_to_action', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))), ('button_group', wagtail.core.blocks.StreamBlock((('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))),))), ('horizontal_rule', base.blocks.breaks.HorizontalRuleBlock()))))))),)))), group='Content')), ('tab_filter', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('unfiltered_tab_text', wagtail.core.blocks.CharBlock(help_text='Text to display on the unfiltered tab (default text: All)', max_length=255, required=False)), ('filtered_content', wagtail.core.blocks.StreamBlock((('filtered_content', wagtail.core.blocks.StructBlock((('tab_text', wagtail.core.blocks.CharBlock(help_text='Text to display on the filter tab', max_length=255)), ('content', wagtail.core.blocks.StreamBlock((('content', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('headline', base.blocks.headings.H2Block()), ('subtitle', base.blocks.headings.H3Block()), ('description', wagtail.core.blocks.RichTextBlock()), ('call_to_action', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))), ('button_group', wagtail.core.blocks.StreamBlock((('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))),))), ('horizontal_rule', base.blocks.breaks.HorizontalRuleBlock())))),), help_text='Content to apply this filter to'))))),), help_text='Filter tabs and the content it applies to')))))), group='Content')), ('popup', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('mp_button_text', wagtail.core.blocks.CharBlock(label='Button Text', max_length=255)), ('mp_button_href', wagtail.core.blocks.PageChooserBlock(label='Popup Content')))))), group='Content')))))))), ('leadership_grid', website.blocks.LeadershipGridBlock())), blank=True)),
                ('violator', models.ForeignKey(blank=True, help_text='(Optional) Show a violator on this page. To create a violator, go to Snippets > Violators', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='overlay.Violator')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField((('flex_container', wagtail.core.blocks.StructBlock((('container_height', wagtail.core.blocks.ChoiceBlock(choices=[(None, 'Automatic'), ('flex-xs', 'Extra Small -- 20% of viewport'), ('flex-sm', 'Small -- 40% of viewport'), ('flex-md', 'Medium -- 50% of viewport'), ('flex-lg', 'Large -- 80% of viewport'), ('flex-xl', 'Extra Large -- 100% of viewport')], required=False)), ('animation_choice', wagtail.core.blocks.ChoiceBlock(choices=[(None, 'None'), ('primary', 'Primary Animation'), ('secondary', 'Secondary Animation'), ('tertiary', 'Tertiary Animation')], required=False)), ('container_classes', wagtail.core.blocks.ListBlock(wagtail.snippets.blocks.SnippetChooserBlock('flex.ContainerCSSClasses', label='Container CSS Classes', required=False), label='(Optional) Additional Container CSS Classes', required=False)), ('flex_items', wagtail.core.blocks.StreamBlock((('media_copy', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('background', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('headline', base.blocks.headings.H2Block()), ('subtitle', base.blocks.headings.H3Block()), ('description', wagtail.core.blocks.RichTextBlock()), ('call_to_action', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))), ('button_group', wagtail.core.blocks.StreamBlock((('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))),))), ('horizontal_rule', base.blocks.breaks.HorizontalRuleBlock())))))))), group='Media')), ('looping_video_copy', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('background', mediatext.blocks.videocopy.LoopingVideoChooserBlock()), ('content', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('headline', base.blocks.headings.H2Block()), ('subtitle', base.blocks.headings.H3Block()), ('description', wagtail.core.blocks.RichTextBlock()), ('call_to_action', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))), ('button_group', wagtail.core.blocks.StreamBlock((('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))),))), ('horizontal_rule', base.blocks.breaks.HorizontalRuleBlock())))))))), group='Media')), ('media_collection', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StreamBlock((('media_items', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.core.blocks.StreamBlock((('heading', base.blocks.headings.H4Block()), ('subheading', base.blocks.headings.H5Block()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))))))))),)))), group='Media')), ('carousel', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('carousel_height', wagtail.core.blocks.ChoiceBlock(choices=[(None, 'Automatic'), ('carousel-xs', 'Extra Small -- 20% of viewport'), ('carousel-sm', 'Small -- 40% of viewport'), ('carousel-md', 'Medium -- 50% of viewport'), ('carousel-lg', 'Large -- 80% of viewport'), ('carousel-xl', 'Extra Large -- 100% of viewport')], required=False)), ('carousel_type', wagtail.core.blocks.ChoiceBlock(choices=[(None, 'Simple'), ('tabbed', 'Tabbed'), ('split', 'Split')], required=False)), ('slides', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('slide_title', wagtail.core.blocks.CharBlock(help_text='Display name for the slide', required=False)), ('content', wagtail.core.blocks.StructBlock((('background', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('headline', base.blocks.headings.H2Block()), ('subtitle', base.blocks.headings.H3Block()), ('description', wagtail.core.blocks.RichTextBlock()), ('call_to_action', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))), ('button_group', wagtail.core.blocks.StreamBlock((('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))),))), ('horizontal_rule', base.blocks.breaks.HorizontalRuleBlock()))))))))))))))), group='Media')), ('iframe', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('iframe_height', wagtail.core.blocks.ChoiceBlock(choices=[(None, 'Automatic'), ('iframe-xs', 'Extra Small -- 20% of viewport'), ('iframe-sm', 'Small -- 40% of viewport'), ('iframe-md', 'Medium -- 50% of viewport'), ('iframe-lg', 'Large -- 80% of viewport'), ('iframe-xl', 'Extra Large -- 100% of viewport')], required=False)), ('iframe_url', wagtail.core.blocks.URLBlock(label='Source URL', required=True)))))), group='Media')), ('vimeo_player', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('height', wagtail.core.blocks.ChoiceBlock(choices=[('xs', 'Extra Small -- 20% of viewport'), ('sm', 'Small -- 40% of viewport'), ('md', 'Medium -- 50% of viewport'), ('lg', 'Large -- 80% of viewport'), ('xl', 'Extra Large -- 100% of viewport')])), ('video_link', wagtail.core.blocks.CharBlock(help_text='The Vimeo ID for the video', label='Video ID', required=True)), ('video', wagtailmedia.blocks.AbstractMediaChooserBlock(help_text='(Optional) Teaser video to use as a background', label='Preview video', required=False)), ('poster_image', wagtail.images.blocks.ImageChooserBlock(help_text='(Optional) Background image that displays while preview video is loading or in place of a preview video if none is specified', required=False)), ('headline', wagtail.core.blocks.RichTextBlock(required=False)), ('cta_copy', wagtail.core.blocks.CharBlock(help_text='(Optional) Play button text. Will use a play icon instead of text if unspecified', label='Play button text', required=False)), ('expanding', wagtail.core.blocks.BooleanBlock(help_text='If checked, video player will expand when clicked rather than constraining the video height', label='Expanding video player', required=False)))))), group='Media')), ('content', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('headline', base.blocks.headings.H2Block()), ('subtitle', base.blocks.headings.H3Block()), ('description', wagtail.core.blocks.RichTextBlock()), ('call_to_action', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))), ('button_group', wagtail.core.blocks.StreamBlock((('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))),))), ('horizontal_rule', base.blocks.breaks.HorizontalRuleBlock()))))), group='Content')), ('contact', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(required=False)), ('address', wagtail.core.blocks.RichTextBlock(required=False)), ('email', wagtail.core.blocks.CharBlock(required=False)), ('phone', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('Phone', wagtail.core.blocks.CharBlock()))))))))), group='Content')), ('tabbed_content', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StreamBlock((('content_tab', wagtail.core.blocks.StructBlock((('tab_text', wagtail.core.blocks.CharBlock(max_length=255)), ('content', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('headline', base.blocks.headings.H2Block()), ('subtitle', base.blocks.headings.H3Block()), ('description', wagtail.core.blocks.RichTextBlock()), ('call_to_action', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))), ('button_group', wagtail.core.blocks.StreamBlock((('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))),))), ('horizontal_rule', base.blocks.breaks.HorizontalRuleBlock()))))))),)))), group='Content')), ('tab_filter', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('unfiltered_tab_text', wagtail.core.blocks.CharBlock(help_text='Text to display on the unfiltered tab (default text: All)', max_length=255, required=False)), ('filtered_content', wagtail.core.blocks.StreamBlock((('filtered_content', wagtail.core.blocks.StructBlock((('tab_text', wagtail.core.blocks.CharBlock(help_text='Text to display on the filter tab', max_length=255)), ('content', wagtail.core.blocks.StreamBlock((('content', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('headline', base.blocks.headings.H2Block()), ('subtitle', base.blocks.headings.H3Block()), ('description', wagtail.core.blocks.RichTextBlock()), ('call_to_action', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))), ('button_group', wagtail.core.blocks.StreamBlock((('button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.CharBlock(icon='edit', max_length=255)), ('button_link', wagtail.core.blocks.URLBlock(required=False))))),))), ('horizontal_rule', base.blocks.breaks.HorizontalRuleBlock())))),), help_text='Content to apply this filter to'))))),), help_text='Filter tabs and the content it applies to')))))), group='Content')), ('popup', wagtail.core.blocks.StructBlock((('flex_grow', wagtail.core.blocks.ChoiceBlock(choices=[('flex-1', '1'), ('flex-2', '2'), ('flex-3', '3'), ('flex-4', '4'), ('flex-5', '5')])), ('content', wagtail.core.blocks.StructBlock((('mp_button_text', wagtail.core.blocks.CharBlock(label='Button Text', max_length=255)), ('mp_button_href', wagtail.core.blocks.PageChooserBlock(label='Popup Content')))))), group='Content')))))))),), blank=True),
        ),
    ]
