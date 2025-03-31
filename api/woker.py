from celery import Celery

# CELERY_RESULT_BACKEND = 'amqp://admin:mypass@rabbit'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_BROKER_URL = 'amqp://admin:mypass@rabbit'

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
