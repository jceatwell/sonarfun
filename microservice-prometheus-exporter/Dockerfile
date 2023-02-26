FROM python:3.8-alpine
ADD requirements.txt /
ADD . /opt/apps
RUN pip install -r requirements.txt
EXPOSE 9877
CMD ["python", "core/exporter.py"]
