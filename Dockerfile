FROM python:3.8

# Install Gunicorn & Gevent
RUN pip3 install gunicorn gevent

COPY requirements.txt ./
RUN pip install --no-cache -r requirements.txt

EXPOSE 5000

COPY . .
CMD ["gunicorn", "--chdir", "./src", "--worker-class", "gevent", "--workers", "4", "--bind", "0.0.0.0:5000", "--preload", "app:app"]