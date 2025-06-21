from celery import Celery
from app import models #Necessário para que o celery reconheça os models do SQLAlchemy

celery = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)
