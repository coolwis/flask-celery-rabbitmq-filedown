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
3) flask-restplus deprected lib
   - error: 
   ImportError: cannot import name 'cached_property'

   - requirements.txt add =>
     Werkzeug==0.16.0
   
```
### Build and Run

```unix
docker-compose up --build
```

To shut down:

 ```unix
docker-compose down
```

### test  
- POST type api
  ```bash
  {
  "task" :"ParseWebLinks",
  "meta": {"url": "www.naver.com"}
  }
  ```
![image](https://github.com/user-attachments/assets/0a0c5bbb-a15d-4390-ad54-d50015a12d8c)

To change the endpoints, update the code in api/app.py

Task changes should happen in celery-queue/{module}/tasks.py
