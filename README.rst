===========
django-furl [WIP]
===========
|Version| |License| |Downloads|

.. |Version| image:: https://img.shields.io/pypi/v/django-furl.svg?style=flat
    :target: https://pypi.python.org/pypi/django-furl
    :alt: Version
.. |License| image:: https://img.shields.io/pypi/l/django-furl.svg?style=flat
    :target: https://github.com/poxip/django-furl/blob/master/LICENSE
    :alt: License
.. |Downloads| image:: https://img.shields.io/pypi/dm/django-furl.svg
    :target: https://pypi.python.org/pypi/django-furl
    :alt: Downloads

**django-furl** is a simple Django wrapper of `Furl
<https://github.com/gruns/furl>`_'s API. It provides essential template tags
for url manipulation.

.. code-block::

    {% furl_add 'http://somestuff.tv/search/?q=The+Office' character='Michael Scott' year=2005 %}

``http://somestuff.tv/search/?q=The+Office&character=Michael+Scott&year=2005``

Installation
------------
::

    $ pip install django-furl


Quick Start
-----------

1. Add "djangofurl" to your INSTALLED_APPS::

    INSTALLED_APPS = [
        ...
        'django_furl',
    ]

2. Load "djangofurl" in your template::

    {% load furl_tags %}


Basic Usage
-----------

.. code-block::

    {% furl_add 'http://somestuff.tv/search/?q=The+Office' character='Michael Scott' year=2005 %}

``http://somestuff.tv/search/?q=The+Office&character=Michael+Scott&year=2005``

.. code-block::

    {% furl_update 'http://somestuff.tv/search/?page=3' q='The Big Bang Theory' character='Sheldon Cooper' page=1 %}

``http://somestuff.tv/search/?page=1&q=The+Big+Bang+Theory&character=Sheldon+Cooper``

.. code-block::

    {% furl_add 'http://somestuff.tv/search/?facets=Type.Other' facets='Category.Drama' q='True Detective' %}

``http://somestuff.tv/search/?facets=Type.Other&facets=Category.Drama&q=True+Detective``

.. code-block::

    {% furl_del 'http://somestuff.tv/search/?facets=Type.Other&facets=Category.Other&q=w' 'facets' 'q' %}

``http://somestuff.tv/search/``
