FROM python:3.9.7   

WORKDIR /
COPY LCS/requirements.txt LCS/requirements.txt
RUN pip install -r LCS/requirements.txt

COPY ./LCS /LCS
WORKDIR /LCS

CMD python manage.py collectstatic --noinput && python manage.py migrate && python server.py
