Django Class Based Views
========================

This is Django Class Based Views taken from Django trunk. Replace all the
references from ``django.views.generic`` to ``cbv`` in the documentation.
All views are available directly from ``cbv`` module, for example::

    from cbv import View, TemplateView

You will need the following middleware installed::

    cbv.middleware.DeferredRenderingMiddleware


`Django Class Based Views Docs <http://docs.djangoproject.com/en/dev/topics/class-based-views/>`_

