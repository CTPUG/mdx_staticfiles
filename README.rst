mdx_staticfiles
===============

.. |staticfiles-ci-badge| image:: https://github.com/CTPUG/mdx_staticfiles/actions/workflows/tests.yml/badge.svg
    :alt: GitHub CI status
    :scale: 100%
    :target:
   https://github.com/CTPUG/mdx_staticfiles/actions/workflows/tests.yml

A Markdown extension to add support for ``django.contrib.staticfiles``.

Licensed under the `ISC License`_.

.. _ISC License: https://github.com/CTPUG/mdx_staticfiles/blob/master/LICENSE


Requirements
============

The mdx_staticfiles plugin requires only the base `markdown`_ library.

.. _markdown: http://pythonhosted.org/Markdown/


Installation
============

Install with ``pip install mdx_staticfiles``.


Documentation
=============

Allows inserting {% static %} Django tags into Markdown, that will
reference files managed by `django.contrib.staticfiles`_.

.. _django.contrib.staticfiles: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/

The following Markdown example:

.. code:: markdown

  A [promotial video]({% static "video/promo.mkv" %}).

Might result in:

.. code:: html

  A <a href="https://cdn.example.net/static/video/promo.mkv">promotional
  video</a>.

Python usage:

.. code:: python

  md = markdown.Markdown(
      extensions=[
          'staticfiles',
      ],
  )
