FROM python:3.6
ADD . /code
WORKDIR /code
RUN pip3 install pipenv
RUN pipenv install
CMD ["pipenv", "run", "{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}.py"]
