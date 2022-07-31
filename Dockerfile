FROM python:3.10.5-alpine3.16

COPY . /usr/src/app/

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

EXPOSE 3000

CMD ["python", "./DeLab.py"]
