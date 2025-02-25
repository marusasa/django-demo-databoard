FROM python:3.13

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


## build container
# docker build -t sasagu/demo-databoard .
#
## publish to docker.io
# docker push sasagu/demo-databoard
#
## run from docker.io
# docker run -d -p 8000:8000 sasagu/demo-databoard