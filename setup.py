import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-furl',
    version='0.1.0',
    include_package_data=True,
    packages=['django_furl', 'django_furl.templatetags'],
    url='https://github.com/poxip/django-furl',
    license='MIT',
    author='Michal Proszek',
    author_email='michal.proszek@gmail.com',
    description='A simple Django extension for url manipulation',
    long_description=README,
    keywords='django url manipulation furl',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
