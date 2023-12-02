from celery import shared_task
from .models import User, Article


@shared_task
def get_all_users():
    return User.objects.all()


@shared_task
def get_one_user(pk: int):
    return User.objects.get(pk=pk)


@shared_task
def create_user_with_validated_data(data: dict):
    return User.objects.create_user(**data)


@shared_task
def get_all_articles():
    return Article.objects.all()


@shared_task
def get_one_article(pk: int):
    return Article.objects.get(pk=pk)


@shared_task
def create_article_with_validated_data(data: dict):
    return Article.objects.create(**data)
