FROM tiangolo/uwsgi-nginx-flask:python3.7

#RUN sudo apt-get update && install --force-yes -y 

WORKDIR /app

COPY requirements.txt /app
RUN python3.7 -m pip install -r requirements.txt

COPY . /app/OnTheRoad
COPY uwsgi.ini /app
