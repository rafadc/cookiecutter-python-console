# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='{{cookiecutter.project_slug}}',
    version='0.1.0',
    description='{{cookiecutter.project_name}}',
    long_description=readme,
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    url='https://github.com/{{cookiecutter.github}}/{{cookiecutter.project_slug}}',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
