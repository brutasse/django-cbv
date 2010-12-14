import logging
from cbv.views.base import View, TemplateView, RedirectView
from cbv.views.dates import *
from cbv.views.detail import DetailView
from cbv.views.edit import CreateView, UpdateView, DeleteView
from cbv.views.list import ListView


class GenericViewError(Exception):
    """A problem in a generic view."""
    pass


class NullHandler(logging.Handler):
    def emit(self, record):
        pass

logging.getLogger('cbv').addHandler(NullHandler())

