FROM python:3.8-alpine
RUN pip install psycopg2-binary
COPY app.py app.py
CMD ["python", "app.py"]