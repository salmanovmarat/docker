FROM ubuntu:xenial-20190515
RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip3 install  django
RUN mkdir PROJECTS
RUN cd /PROJECTS
COPY . /PROJECTS/
RUN pip3 install -r /PROJECTS/first_project/requirements.txt
RUN python3 /PROJECTS/first_project/manage.py migrate
CMD ["python3", "/PROJECTS/first_project/manage.py","runserver", "0.0.0.0:8000"]