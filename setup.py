from pathlib import Path
from setuptools import setup

setup_url = 'https://github.com/josepsanz/python-template'
setup_name = 'python-template'
setup_author = 'Josep Maria Sanz Xicola'
setup_author_email = 'jmsanz83@gmail.com'
###

with open('requirements.txt', 'r') as f:
    requirements = tuple(f.readlines())

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with (Path(f'mysweetcode') / '_version.py').open() as f:
    _vars = dict()
    exec(f.read(), _vars)
    version = _vars.get('__version__', '0.0.0')
    del _vars

setup(
    name=setup_name,
    version=version,

    install_requires=requirements,
    include_package_data=True,
    package_data={
        'mysweetcode': []
    },
    url=setup_url,
    author=setup_author,
    author_email=setup_author_email,
    description='A little template for packaging python code',
    long_description=long_description
)
