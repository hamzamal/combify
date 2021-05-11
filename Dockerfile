  
FROM python:3.7

WORKDIR /app

RUN pip install pandas scikit-learn flask gunicorn keras tensorflow

ADD model.json model.json
ADD model.h5 model.h5
ADD server.py server.py

EXPOSE 5000

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "server:app" ]
