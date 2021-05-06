  
FROM python:3.7

WORKDIR /app

RUN pip install pandas scikit-learn flask gunicorn keras

ADD rf_model.sav rf_model.sav
ADD server.py server.py

EXPOSE 5000

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "server:app" ]
