FROM python:alpine3.7 
COPY . /Reliant/
EXPOSE 5000
WORKDIR /Reliant/
RUN pip install -r requirements.txt 
CMD python runserver.py