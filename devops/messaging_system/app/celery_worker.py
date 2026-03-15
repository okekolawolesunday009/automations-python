from celery import Celery

celery_app = Celery(
    "worker",
    broker="amqp://guest:guest@rabbitmq:5672//",
    backend="rpc://"
)

celery_app.conf.task_routes = {
    "app.tasks.send_email": {"queue": "emails"}
}