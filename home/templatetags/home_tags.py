from django import template
from django.urls import translate_url
from wagtail.core.models import Locale, Site

from home.models import SectionIndexPage, Section, Article, FooterIndexPage
from iogt.settings.base import LANGUAGES

register = template.Library()


@register.inclusion_tag('home/tags/language_switcher.html', takes_context=True)
def language_switcher(context, page):
    if page:
        context.update({
            'translations': page.get_translations(inclusive=True).all(),
        })
    context.update({'default_locales': Locale.objects.all()})

    return context


@register.inclusion_tag('home/tags/previous-next-buttons.html')
def render_previous_next_buttons(page):
    return {
        'next_sibling': page.get_next_siblings().live().first(),
        'previous_sibling': page.get_prev_siblings().live().first()
    }


@register.inclusion_tag('home/tags/footer.html', takes_context=True)
def footer(context):
    return {
        'footer_pages': FooterIndexPage.get_active_footers(),
        'request': context['request'],
    }


@register.inclusion_tag('home/tags/top_level_sections.html', takes_context=True)
def top_level_sections(context):
    return {
        'top_level_sections': SectionIndexPage.get_top_level_sections(),
        'request': context['request'],
    }


@register.inclusion_tag('home/tags/banners_list.html')
def render_banners_list(banners):
    return {'banners': banners}


@register.inclusion_tag('home/tags/articles_list.html', takes_context=True)
def render_articles_list(context, articles):
    context.update({
        'articles': articles,
    })
    return context


@register.inclusion_tag('home/tags/featured_content_list.html')
def render_featured_content_list(featured_content):
    return {'featured_content_items': featured_content}


@register.inclusion_tag('home/tags/sub_sections.html')
def render_sub_sections_list(sub_sections):
    return {'sub_sections': sub_sections}


@register.inclusion_tag('home/tags/polls.html')
def render_polls_list(polls):
    return {'polls': polls}


@register.inclusion_tag('home/tags/questionnaire.html')
def render_questionnaire_list(questionnaire):
    return {'questionnaire': questionnaire}


@register.inclusion_tag('home/tags/section_progress.html')
def render_user_progress(user_progress, show_count=True):
    return {
        **user_progress,
        'show_count': show_count,
    }


@register.inclusion_tag('home/tags/is_completed.html', takes_context=True)
def render_is_content_completed(context, content):
    content = content.specific
    if isinstance(content, (Section, Article)):
        context.update({
            'is_completed': content.is_completed(context['request'])
        })
    return context


@register.inclusion_tag('home/tags/sub_sections.html', takes_context=True)
def render_sub_sections_list(context, sub_sections):
    context.update({
        'sub_sections': sub_sections,
    })
    return context


@register.simple_tag
def locale_set(locale, url):
    for item in LANGUAGES:
        code = item[0]
        url = url.replace(f"/{code}/", "")
    return f'/{locale}/{url}'


@register.simple_tag
def translated_home_page_url(language_code):
    locale = Locale.objects.get(language_code=language_code)
    default_home_page = Site.objects.filter(is_default_site=True).first().root_page
    home_page = default_home_page.get_translation_or_none(locale)
    page = home_page or default_home_page
    return page.url


@register.simple_tag(takes_context=True)
def change_lang(context, lang=None, *args, **kwargs):
    path = context['request'].path
    return translate_url(path, lang)


@register.simple_tag
def get_menu_icon(menu_item):
    if hasattr(menu_item.icon, 'url'):
        return menu_item.icon.url
    elif hasattr(menu_item, 'link_page') and isinstance(menu_item.link_page, Section) and hasattr(
            menu_item.link_page.icon, 'url'):
        return menu_item.link_page.specific.icon.url

    return ''


@register.inclusion_tag('wagtailadmin/shared/field_as_li.html')
def render_external_link_with_help_text(field):
    field.help_text = f'If you are linking back to a URL on your own IoGT site, be sure to remove the domain and ' \
                      f'everything before it. For example "http://sd.goodinternet.org/url/" should instead be "/url/".'

    return {'field': field, 'red_help_text': True}


@register.inclusion_tag('wagtailadmin/shared/field_as_li.html')
def render_redirect_from_with_help_text(field):
    field.help_text = f'A relative path to redirect from e.g. /en/youth. ' \
                      f'See "https://docs.wagtail.io/en/stable/editor_manual/managing_redirects.html" for more details.'

    return {'field': field, 'red_help_text': True}
