FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./OnTheRoad /app/OnTheRoad
COPY uwsgi.ini /app
