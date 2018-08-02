from setuptools import setup
import codecs
from fns import __version__

with codecs.open('README.md', 'r', 'utf-8') as readme:
    long_description = readme.read()

setup(
    name='fns',
    version=__version__,
    description='Revise receipt client',
    author='Sergey Popov',
    author_email='poserg@gmail.com',
    license='MIT License',
    url='https://github.com/poserg/revise-receipt-client/',
    packages=[
        'fns',
    ],
    long_description=long_description,
    install_requires=[
        'requests',
    ],
)
