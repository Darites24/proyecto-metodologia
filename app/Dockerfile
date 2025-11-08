FROM python:3.13
WORKDIR /app_cd
COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "manage.py", "runserver" ]

