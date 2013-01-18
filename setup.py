# -*- coding: utf-8 -*-
"""Setup file for easy installation"""
from os.path import join, dirname
from setuptools import setup, find_packages


version = __import__('media_renderer').__version__

LONG_DESCRIPTION = """
django media renderer is an easy way of bringing rendering js and css files
with the django templates renderer

built for single page applications where pages do not change regularly
but tags such as url and include are very useful
"""


def long_description():
    """Return long description from README.rst if it's present
    because it doesn't get installed."""
    try:
        return open(join(dirname(__file__), 'README.rst')).read()
    except IOError:
        return LONG_DESCRIPTION


setup(name='django-media-renderer',
      version=version,
      author='Fred Kingham',
      author_email='fredkingham@gmail.com',
      description='simple method for rendering templates',
      license='BSD',
      keywords='django, media, templates, render',
      url='https://github.com/fredkingham/media_renderer',
      packages=find_packages(),
      include_package_data=True,
      long_description=long_description(),
      install_requires=['django>=1.4.0'],
      classifiers=['Framework :: Django',
                   'Development Status :: 4 - Beta',
                   'Topic :: Internet',
                   'License :: OSI Approved :: BSD License',
                   'Intended Audience :: Developers',
                   'Environment :: Web Environment',
                   'Programming Language :: Python :: 2.5',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7'])
