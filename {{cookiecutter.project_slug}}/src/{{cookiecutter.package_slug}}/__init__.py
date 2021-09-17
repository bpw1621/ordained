"""Top-level {{cookiecutter.package_slug}} package."""

import logging
from logging import NullHandler

__author__ = '{{cookiecutter.full_name}}'
__email__ = '{{cookiecutter.email}}'
__version__ = '{{cookiecutter.version}}'

logging.getLogger(__name__).addHandler(NullHandler())
