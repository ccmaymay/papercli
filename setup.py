from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup


__version__ = '0.1b0'


packages = [
    'papercli',
]

scripts = ['scripts/bs']


setup(
    name='papercli',
    version=__version__,
    description='Mendeley paper manager',
    url='https://bitbucket.org/cjmay4754/papercli',
    packages=packages,
    scripts=scripts,
    install_requires=[
        'mendeley>=0.3.0',
    ],
    license='Apache',
)
