Django Class Based Views
========================

This is Django Class Based Views taken from Django trunk.

Use CBVs like this::

    import cbv as generic

Then write your class-based views as expained in the `Django documentation`_::

    class SomeView(generic.TemplateView):
        template_name = 'some_template.html'

.. _Django documentation: http://docs.djangoproject.com/en/dev/topics/class-based-views

You will need the following middleware installed::

    cbv.middleware.DeferredRenderingMiddleware

Once you're ready to use Django 1.3, you'll only need to switch the import
statement to::

    from django.views import generic
