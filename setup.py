from setuptools import setup


__version__ = '0.1'


setup(
    name='papercli',
    version=__version__,
    description='little Mendeley CLI',
    scripts=['scripts/papercli'],
    install_requires=[
        'mendeley>=0.3.2',
    ],
    url='https://github.com/cjmay/papercli',
    license='BSD',
)
