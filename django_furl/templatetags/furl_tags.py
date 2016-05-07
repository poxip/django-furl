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
    Add url params to an existing url. Similar to `furl_update`.

    :param str url - The url to process.
    :param kwargs - The dictionary of parameters to add to the url
        (if the specified parameter is present in the url, it is duplicated).
    :return The updated url.
    """
    url = furl(url)
    return url.add(kwargs)


@register.simple_tag
def furl_del(url, *args):
    """
    Remove url params from an existing url. Similar to `furl_update`.

    :param str url - The url to process.
    :param args - The list of parameters to remove from the url.
    :return The updated url.
    """
    url = furl(url)
    return url.remove(args)


# Template Filters

def parse_arg(arg):
    arg = arg.split('=')
    return {arg[0].strip(): arg[1].strip()}


@register.filter
def f_update(url, arg):
    """
    Add url params to an existing url

    :param str url - The url to process.
    :param str arg - The key=value string describing the parameter being added.
    :return The updated url.
    """
    return furl_update(url, **parse_arg(arg))


@register.filter
def f_add(url, arg):
    """
    Add url params to an existing url. Similar to `f_update`.

    :param str url - The url to process.
    :param str arg - The key=value string describing the parameter being added.
        If the parameter is present in the url, it's duplicated.
    :return The updated url.
    """
    return furl_add(url, **parse_arg(arg))


# filter('f_del', furl_del) does not work here
register.filter('f_del', lambda url, arg: furl_del(url, arg))
