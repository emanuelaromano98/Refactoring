FROM python:3.12-alpine

EXPOSE 5001/tcp

WORKDIR /app

RUN pip install flask

COPY plot.html .

COPY app.py .

CMD [ "python", "./app.py" ]
