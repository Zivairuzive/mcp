FROM python:3-slim 
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn sqlalchemy

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--reload" ]