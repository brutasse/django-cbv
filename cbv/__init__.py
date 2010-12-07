import logging
from cbv.base import View, TemplateView, RedirectView
from cbv.dates import *
from cbv.detail import DetailView
from cbv.edit import CreateView, UpdateView, DeleteView
from cbv.list import ListView


class GenericViewError(Exception):
    """A problem in a generic view."""
    pass


class NullHandler(logging.Handler):
    def emit(self, record):
        pass

logging.getLogger('cbv').addHandler(NullHandler())

