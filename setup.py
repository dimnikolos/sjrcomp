try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'sjrcomp',
    'author': 'sjrcomp',
    'url': 'http://github.com/dimnikolos',
    'download_url': 'http://github.com/dimnikolos',
    'author_email': 'dnikolos@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['sjrcomp'],
    'scripts': [],
    'name': 'sjrcomp'
}

setup(**config)