"""Template tag wrappers for furl's API"""

from django import template
from furl import furl

register = template.Library()


@register.simple_tag
def furl_update(url, **kwargs):
    """
    Update url params

    :param str url - The url to process.
    :param kwargs - The dictionary of parameters to update the url from
        (if the specified parameter is present in the url, it is changed).
    :return The updated url.
    """
    url = furl(url)
    url.args.update(kwargs)
    return url


@register.simple_tag
def furl_add(url, **kwargs):
    """
    Add url params to an existing url. Similar to `url_param`.

    :param str url - The url to process.
    :param kwargs - The dictionary of parameters to add to the url
        (if the specified parameter is present in the url, it is duplicated).
    :return The updated url.
    """
    url = furl(url)
    return url.add(kwargs)