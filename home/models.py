from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from blog.models import BlogPage

class HomePage(Page):
    body = RichTextField(blank=True)

    masthead = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def get_context(self, request):
        context = super().get_context(request)
        blogpages = BlogPage.objects.live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        ImageChooserPanel('masthead'),
    ]

class OtherPage(Page):
    intro = models.CharField(max_length=250, blank=True)
    body = RichTextField(blank=True)
    body2 = RichTextField(blank=True)

    masthead = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    portrait = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        FieldPanel('body2', classname="full"),
        ImageChooserPanel('masthead'),
        ImageChooserPanel('portrait'),
    ]