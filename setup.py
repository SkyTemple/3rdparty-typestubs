__version__ = '1.0.0'

from setuptools import setup, find_packages

setup(
    name='skytemple-3rdparty-typestubs',
    version=__version__,
    packages=find_packages(),
    package_data={p: ['py.typed'] for p in find_packages()},
    description='(Minimal) PEP 561 type stubs for libraries SkyTemple uses',
    url='https://github.com/SkyTemple/skytemple_/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
    ],
)
