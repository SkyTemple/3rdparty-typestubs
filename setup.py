__version__ = '1.0.0.post1'

from setuptools import setup, find_packages

setup(
    name='skytemple-3rdparty-typestubs',
    version=__version__,
    packages=['ndspy'],
    package_data={'ndspy': ['py.typed', '*.pyi']},
    description='(Minimal) PEP 561 type stubs for libraries SkyTemple uses',
    url='https://github.com/SkyTemple/skytemple_/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
    ],
)
