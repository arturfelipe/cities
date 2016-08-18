import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='cities',
    version='0.0.1',
    description='Load data from cities and countries all over the world',
    author='Artur Sousa',
    author_email='arturfelipe.sousa@gmail.com',
    url='https://github.com/arturfelipe/cities',
    packages=[
        'cities',
    ],
    package_dir={'cities': 'cities'},
    install_requires=[
        'requests',
    ],
    include_package_data=True,
    zip_safe=False,
    long_description=read('README.md'),
    license='MIT',
    keywords='cities countries'
)
