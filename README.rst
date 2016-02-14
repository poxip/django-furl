===========
django-furl
===========

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
