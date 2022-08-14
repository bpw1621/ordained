"""Top-level {{cookiecutter.package_slug}} package."""

import logging
from logging import NullHandler

try:
    from importlib import metadata
except ImportError:
    import importlib_metadata as metadata

__author__ = '{{cookiecutter.full_name}}'
__email__ = '{{cookiecutter.email}}'
__version__ = metadata.version('{{cookiecutter.package_slug}}')

logging.getLogger(__name__).addHandler(NullHandler())
