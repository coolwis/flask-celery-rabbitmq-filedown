# Flask Celery RabbitMQ

A basic [Docker Compose](https://docs.docker.com/compose/) template for orchestrating a [Flask](http://flask.pocoo.org/) application & a [Celery](http://www.celeryproject.org/) queue with [RabbitMQ](https://www.rabbitmq.com/).

## Installation

```unix
  
원본:  git clone https://github.com/ChenYuTingJerry/flask-celery-rabbitmq.git
git clone https://github.com/coolwis/flask-celery-rabbitmq-filedown.git
```

## bug Fix 
```bash
1) backend redis로 수정,  rabbitmq 에러남
  CELERY_RESULT_BACKEND = 'redis://redis:6379'

2) celery-queue/dockerfile 수정: worker 실행 명령문
   # ENTRYPOINT ["celery", "worker", "--app=celery_worker.app", "--loglevel=info"]
   ENTRYPOINT ["celery","-A","celery_worker", "worker", "--loglevel=info"]
   
```
### Build and Run

```unix
docker-compose up --build
```

To shut down:

 ```unix
docker-compose down
```

To change the endpoints, update the code in api/app.py

Task changes should happen in celery-queue/{module}/tasks.py
