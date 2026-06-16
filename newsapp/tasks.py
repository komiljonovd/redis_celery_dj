from .models import News
from celery import shared_task

@shared_task
def publish_news(news_id):
    news = News.objects.filter(pk=news_id,is_published=False).update(is_published=True)
    print('Done' if news==1 else 'No updated')

@shared_task(ignore_result=True)
def publish_all_news() -> None:
    news = News.objects.filter(is_published=False).update(is_published=True)
    print('all news published')