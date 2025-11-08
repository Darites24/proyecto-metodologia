FROM python:3.13

WORKDIR /app

COPY app/ /app/
COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

CMD ["gunicorn", "conversorDivisas.wsgi:application", "--bind", "0.0.0.0:8000"]