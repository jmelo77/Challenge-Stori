FROM python:3.10.5-bullseye

WORKDIR /challenge-stori

COPY ./requirements.txt /challenge-stori/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /challenge-stori/app
 
COPY .env /challenge-stori/.env

EXPOSE 5000

ENV PYTHONPATH "${PYTHONPATH}:/challenge-stori/app"

CMD ["gunicorn", "-b", "0.0.0.0:5000", "manage:app"]