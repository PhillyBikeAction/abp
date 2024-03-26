from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.contrib.typed_table_block.blocks import TypedTableBlock
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index


class AlignedParagraphBlock(blocks.StructBlock):
    """
    RichTextBlock that can be aligned.
    """

    alignment = blocks.ChoiceBlock(
        choices=[("left", "Left"), ("center", "Center"), ("right", "Right")],
        default="left",
    )
    paragraph = blocks.RichTextBlock()

    class Meta:
        template = "blocks/aligned_paragraph.html"


_features = [
    "h2",
    "h3",
    "h4",
    "bold",
    "italic",
    "ol",
    "ul",
    "hr",
    "link",
    "document-link",
    "image",
    "embed",
    "code",
    "blockquote",
]


class NavigationContainerPage(Page):
    """
    This page doesn't have HTML, and it works only to support hierarchical
    structure of the site.
    """

    class Meta:
        verbose_name = "Navigation Container Page"

    subpage_types = ["NavigationContainerPage", "PbaStreamPage"]


class PbaStreamPage(Page):
    """
    Model to hold content for the many possible pages in the conference
    """

    body = StreamField(
        [
            ("paragraph", AlignedParagraphBlock(features=_features)),
            ("html", blocks.RawHTMLBlock()),
            ("table", TableBlock()),
            ("typed_table_block", TypedTableBlock([
                ('rich_text', blocks.RichTextBlock()),
                ('image', ImageChooserBlock()),
                ("html", blocks.RawHTMLBlock()),
            ])),
        ],
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body", classname="full"),
    ]

    subpage_types = ["NavigationContainerPage", "PbaStreamPage"]

    template = "cms/stream_page.html"

    class Meta:
        verbose_name = "Stream Page"


class WelcomePbaStreamPage(Page):
    """
    Model to hold content for a simpler page, with different styling
    """

    intro = StreamField(
        [
            ("paragraph", AlignedParagraphBlock(features=_features)),
            ("html", blocks.RawHTMLBlock()),
        ],
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full"),
    ]

    subpage_types = ["NavigationContainerPage", "PbaStreamPage"]

    template = "cms/welcome_stream_page.html"

    class Meta:
        verbose_name = "Welcome Stream Page"
