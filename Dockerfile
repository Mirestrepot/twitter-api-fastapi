FROM python:3.11

WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./backend /code/backend
#CMD ["uvicorn", "backend.app:app", "--proxy-headers","--host", "0.0.0.0", "--port", "80"]
CMD ["python", "./backend/main.py"]

#To update repository
#docker build -t app-update .
#docker create --name docker-container -p 80:
#docker start docker-container
#docker commit docker-container mirestrepot/twitter-api-fastapi:latest