FROM python:3.9
WORKDIR /dj
COPY ./requirements.txt /dj/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /dj/requirements.txt
COPY ./back /dj/back
CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"]