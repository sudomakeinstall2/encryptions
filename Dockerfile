FROM python:3.7

COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000
ADD . /app
CMD python app.py